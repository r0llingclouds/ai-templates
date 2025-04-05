import logging
import time
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

# Import necessary docling components
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorDevice,
    AcceleratorOptions,
    PdfPipelineOptions,
    TableStructureOptions,
)

# tqdm for progress bars
try:
    from tqdm.notebook import tqdm
except ImportError:
    print("Consider installing tqdm for progress bars: pip install tqdm")
    def tqdm(iterable, *args, **kwargs):
        return iterable

# Configure logging (optional)
logging.basicConfig(level=logging.WARNING) # Set to WARNING for less verbose default output
_log = logging.getLogger(__name__)

class DoclingProcessor:
    """
    Processes PDF files using the Docling library to extract content as Markdown.
    Includes optional functionality to save markdown files to disk.

    Basic Usage:
    -----------
    1. Instantiate the class:
       >>> processor = DoclingProcessor()

    2. Prepare a list of PDF file paths (strings):
       >>> pdf_list = ["/path/to/doc1.pdf", "/path/to/doc2.pdf"]

    3. Call the process_files method:
       >>> results = processor.process_files(pdf_list)

    Optional Features:
    -----------------
    - **Custom Settings:** Override default processing options (like OCR language,
      disabling table detection, accelerator options, etc.) by passing a
      'settings' dictionary to the process_files method. The structure
      mirrors the 'default_settings' attribute.
      >>> custom_settings = {
      ...     "do_ocr": True,
      ...     "ocr_options": {"lang": ["en", "fr"]}, # Process English and French
      ...     "do_table_structure": False, # Disable table processing
      ...     "accelerator_options": {"num_threads": 2}
      ... }
      >>> results = processor.process_files(pdf_list, settings=custom_settings)

    - **Saving Markdown:** Automatically save successfully extracted Markdown
      to files by providing an output directory path via the 'output_dir'
      parameter in the process_files method.
      >>> output_folder = "./markdown_output"
      >>> results = processor.process_files(pdf_list, output_dir=output_folder)
      # Files like "doc1.md", "doc2.md" will be saved in ./markdown_output

    Return Value:
    ------------
    The `process_files` method returns a list of dictionaries, one for each
    input file. Each dictionary contains the following keys:
     - 'source_file' (str): The original path of the processed PDF.
     - 'markdown_content' (Optional[str]): Extracted Markdown text, or None if failed.
     - 'processing_time' (float): Time taken for the file conversion in seconds.
     - 'error' (Optional[str]): Processing error message if conversion failed, else None.
     - 'save_error' (Optional[str]): Saving error message if saving was attempted
                                       and failed, else None.

    Example Iterating Results:
    -------------------------
    >>> for item in results:
    ...     print(f"File: {item['source_file']}")
    ...     if item['error']:
    ...         print(f"  Processing Error: {item['error']}")
    ...     elif item['markdown_content']:
    ...         print(f"  Success ({item['processing_time']:.2f}s)")
    ...         # print(item['markdown_content'][:100] + "...") # Access content
    ...         if item['save_error']:
    ...             print(f"  Saving Error: {item['save_error']}")
    ...         elif output_folder: # Check if saving was attempted
    ...             print("  Saved successfully.") # Assumes output_folder was set
    ...     else: # Should not happen if error is None, but as safeguard
           print("  No markdown content and no processing error reported.")

    """

    def __init__(self):
        """
        Initializes the DoclingProcessor with default pipeline settings.
        """
        self.default_settings = {
            "do_ocr": True,
            "do_table_structure": True,
            "table_structure_options": {
                "do_cell_matching": True,
            },
            "ocr_options": {
                "lang": ["en"],
            },
            "accelerator_options": {
                "num_threads": 4,
                "device": "AUTO",
            },
        }
        # You can inspect processor.default_settings to see the structure
        # expected by the 'settings' parameter in process_files.

    def _create_pipeline_options(self, settings: Dict[str, Any]) -> PdfPipelineOptions:
        """Helper method to construct PdfPipelineOptions from settings dictionary."""
        # This internal method merges provided settings with defaults.
        pipeline_options = PdfPipelineOptions()
        merged_settings = {**self.default_settings, **settings}

        pipeline_options.do_ocr = merged_settings.get("do_ocr", True)
        pipeline_options.do_table_structure = merged_settings.get("do_table_structure", True)

        if pipeline_options.do_table_structure:
            table_opts_settings = merged_settings.get("table_structure_options", self.default_settings["table_structure_options"])
            table_structure_options = TableStructureOptions()
            table_structure_options.do_cell_matching = table_opts_settings.get("do_cell_matching", True)
            pipeline_options.table_structure_options = table_structure_options

        if pipeline_options.do_ocr:
            ocr_opts_settings = merged_settings.get("ocr_options", self.default_settings["ocr_options"])
            pipeline_options.ocr_options.lang = ocr_opts_settings.get("lang", ["en"])

        accel_opts_settings = merged_settings.get("accelerator_options", self.default_settings["accelerator_options"])
        device_str = accel_opts_settings.get("device", "AUTO").upper()
        try:
            device = AcceleratorDevice[device_str]
        except KeyError:
            _log.warning(f"Invalid accelerator device '{device_str}'. Falling back to AUTO.")
            device = AcceleratorDevice.AUTO
        pipeline_options.accelerator_options = AcceleratorOptions(
            num_threads=accel_opts_settings.get("num_threads", 4),
            device=device
        )
        return pipeline_options

    def process_files(
        self,
        pdf_files: List[str],
        settings: Optional[Dict[str, Any]] = None,
        output_dir: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Processes a list of PDF files using Docling and returns extracted Markdown.
        Optionally saves the markdown files to the specified output directory.

        Args:
            pdf_files: A list of paths (strings) to the PDF files to process.
            settings: Optional dict to override default processing settings.
                      See class docstring or self.default_settings for structure.
            output_dir: Optional path (string) to a directory where successfully
                        extracted markdown files should be saved (.md extension).
                        If None, files are not saved automatically.

        Returns:
            List of dictionaries, one per input file (see class docstring for details).
        """
        current_settings = settings or {}
        processed_documents = []
        output_dir_path = None

        # Prepare output directory if specified
        if output_dir:
            try:
                output_dir_path = Path(output_dir)
                output_dir_path.mkdir(parents=True, exist_ok=True)
                _log.info(f"Markdown files will be saved to: {output_dir_path.resolve()}")
            except Exception as e:
                _log.error(f"Failed to create or access output directory '{output_dir}': {e}. Files will not be saved.")
                output_dir_path = None # Disable saving

        # Initialize Docling converter
        try:
            pipeline_options = self._create_pipeline_options(current_settings)
            doc_converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
            _log.info(f"Docling converter initialized with options: {pipeline_options}")
        except Exception as e:
            _log.error(f"Failed to initialize DocumentConverter: {e}")
            for filepath in pdf_files:
                 processed_documents.append({
                    "source_file": filepath, "markdown_content": None,
                    "processing_time": 0.0, "error": f"Initialization failed: {e}",
                    "save_error": None
                })
            return processed_documents

        # Process files
        for filepath in tqdm(pdf_files, desc="Processing PDFs"):
            start_time = time.time()
            markdown_content = None
            processing_error = None
            save_error = None
            input_doc_path = Path(filepath)

            if not input_doc_path.is_file():
                 processing_error = "File not found."
                 _log.warning(f"Skipping non-existent file '{filepath}'")
                 processing_time = 0.0
            else:
                # Attempt conversion
                try:
                    conv_result = doc_converter.convert(input_doc_path)
                    markdown_content = conv_result.document.export_to_markdown()
                except Exception as e:
                    processing_error = str(e)
                    _log.error(f"Error processing file '{filepath}': {e}", exc_info=False)
                processing_time = time.time() - start_time

                # Attempt to save if conversion succeeded and output dir is set
                if not processing_error and markdown_content and output_dir_path:
                    try:
                        output_filename = input_doc_path.stem + ".md"
                        output_filepath = output_dir_path / output_filename
                        output_filepath.write_text(markdown_content, encoding='utf-8')
                        _log.info(f"Saved: '{output_filepath}'")
                    except Exception as e:
                        save_error = f"Failed to save file: {e}"
                        _log.warning(f"Error saving markdown for '{filepath}': {save_error}")

            processed_documents.append({
                "source_file": filepath,
                "markdown_content": markdown_content,
                "processing_time": round(processing_time, 2),
                "error": processing_error,
                "save_error": save_error,
            })

        return processed_documents

print("DoclingProcessor class defined with usage comments in the docstring.")

# You can view the main docstring in Jupyter/IPython by running:
# DoclingProcessor?
# or
# help(DoclingProcessor)