from typing import List, Dict, Any
from pdf_chunker.pdf_manager import PDFManager
from tqdm import tqdm
import os


class PDFChunker:
    """Implementation using PDFChunker approach"""

    def __init__(self):
        self.default_settings = {
            "remove_header_footer": {
                "enabled": False,
                "header_regex": "",
                "footer_regex": "",
            },
            "join_pages": {"enabled": True},
            "remove_matches": {"enabled": False, "regex_patterns": [""]},
            "split_section": {"enabled": False, "section_regex": ""},
            "split_paragraphs": {"enabled": True},
            "split_chunk": {
                "enabled": True,
                "chunk_token_size": 512,
                "chunk_overlap": 30,
            },
            "sentence_cleaner": {"enabled": True},
        }

    def process_files(
        self, pdf_files: List[str], settings: Dict[str, Any] = None
    ) -> List[Dict]:
        # Merge default settings with provided settings
        settings = {**self.default_settings, **(settings or {})}

        chunks = []
        for filepath in tqdm(pdf_files):
            try:
                pdf_manager = PDFManager(filepath, **settings)
                text_chunks = pdf_manager.extract_chunks()
                for chunk in text_chunks:
                    # Create chunk dictionary with metadata
                    chunks.append(
                        {
                            "document_title": chunk.document_name,
                            "text": chunk.text,
                            "document_page": chunk.page_number,
                            "n_tokens": len(chunk.text.split()),
                        }
                    )
            except Exception as e:
                print(f"Error procesando: '{os.path.basename(filepath)}': {e}")

        for i, chunk in enumerate(chunks):
            chunk["chunk_id"] = i
            chunk["document_id"] = hash(chunk["document_title"]) % (10**8)
        return chunks
