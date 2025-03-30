import pymupdf
from typing import List, Dict, Optional
from tqdm import tqdm
import os
import re


class PyMuPDFProcessor:
    def __init__(self):
        pass

    def process_files(
        self,
        pdf_files: List[str],
        max_chunk_length: Optional[int] = None,
        output_folder: Optional[str] = None
    ) -> List[Dict]:
        """
        Processes a list of PDF files, extracting text and images.

        Args:
            pdf_files (List[str]): List of paths to PDF files.
            max_chunk_length (Optional[int]): Maximum number of tokens per chunk.
                                              If not provided, processes per page.
            output_folder (Optional[str]): Optional folder to save images.
                                           Defaults to individual folders per PDF file.

        Returns:
            List[Dict]: List of dictionaries containing extracted text and metadata.
        """
        results = []
        chunk_id_counter = 0  # To keep track of chunk IDs

        for filepath in tqdm(pdf_files):
            try:
                document_title = os.path.basename(filepath)
                pdf_base_name = os.path.splitext(document_title)[0]
                document_id = hash(document_title) % (10 ** 8)

                # Set up output paths for images
                if output_folder:
                    image_folder = os.path.join(output_folder, f"{pdf_base_name}_images")
                else:
                    image_folder = f"{pdf_base_name}_images"

                # Create the image folder if it doesn't exist
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)

                with pymupdf.open(filepath) as pdf_document:
                    for page_num in range(pdf_document.page_count):
                        try:
                            page = pdf_document.load_page(page_num)
                            page_text = page.get_text("text")

                            if not page_text.strip():
                                continue  # Skip empty pages

                            # Extract images from the page
                            image_list = page.get_images(full=True)
                            for img_index, img in enumerate(image_list):
                                xref = img[0]
                                base_image = pdf_document.extract_image(xref)
                                image_bytes = base_image["image"]
                                image_extension = base_image["ext"]

                                # Save the images
                                image_filename = f"image_page_{page_num + 1}_{img_index}.{image_extension}"
                                image_path = os.path.join(image_folder, image_filename)
                                with open(image_path, 'wb') as image_file:
                                    image_file.write(image_bytes)

                            if max_chunk_length is not None:
                                # Process text with chunk length control
                                paragraphs = re.split(r'\n\s*\n', page_text.strip())
                                paragraphs = [p.strip() for p in paragraphs if p.strip()]

                                chunk_text = ''
                                chunk_token_count = 0

                                for paragraph in paragraphs:
                                    paragraph_tokens = paragraph.split()
                                    paragraph_token_count = len(paragraph_tokens)

                                    if chunk_token_count + paragraph_token_count <= max_chunk_length:
                                        # Add paragraph to current chunk
                                        if chunk_text:
                                            chunk_text += '\n\n' + paragraph
                                        else:
                                            chunk_text = paragraph
                                        chunk_token_count += paragraph_token_count
                                    else:
                                        if chunk_text:
                                            # Finish current chunk and start a new one
                                            results.append({
                                                'chunk_id': chunk_id_counter,
                                                'document_id': document_id,
                                                'document_title': document_title,
                                                'document_page': page_num + 1,
                                                'text': chunk_text.strip(),
                                                'n_tokens': chunk_token_count
                                            })
                                            chunk_id_counter += 1
                                        # Handle paragraphs longer than max_chunk_length
                                        if paragraph_token_count > max_chunk_length:
                                            start = 0
                                            while start < paragraph_token_count:
                                                end = min(start + max_chunk_length, paragraph_token_count)
                                                chunk_tokens = paragraph_tokens[start:end]
                                                chunk_text = ' '.join(chunk_tokens)
                                                n_chunk_tokens = len(chunk_tokens)
                                                results.append({
                                                    'chunk_id': chunk_id_counter,
                                                    'document_id': document_id,
                                                    'document_title': document_title,
                                                    'document_page': page_num + 1,
                                                    'text': chunk_text.strip(),
                                                    'n_tokens': n_chunk_tokens
                                                })
                                                chunk_id_counter += 1
                                                start = end
                                            chunk_text = ''
                                            chunk_token_count = 0
                                        else:
                                            chunk_text = paragraph
                                            chunk_token_count = paragraph_token_count

                                # Save any remaining chunk
                                if chunk_text:
                                    results.append({
                                        'chunk_id': chunk_id_counter,
                                        'document_id': document_id,
                                        'document_title': document_title,
                                        'document_page': page_num + 1,
                                        'text': chunk_text.strip(),
                                        'n_tokens': chunk_token_count
                                    })
                                    chunk_id_counter += 1
                            else:
                                # Process per page
                                results.append({
                                    "doc_name": pdf_base_name,
                                    "doc_page": page_num + 1,
                                    "text": page_text
                                })
                        except Exception as e:
                            print(f"Error processing page {page_num + 1} in '{document_title}': {e}")
                            continue

                    print(f"Processed: {filepath}")
                    print(f"Text extracted for {pdf_document.page_count} pages.")
                    print(f"Images saved in: {image_folder}")

            except Exception as e:
                print(f"Error opening '{document_title}': {e}")
                continue

        return results