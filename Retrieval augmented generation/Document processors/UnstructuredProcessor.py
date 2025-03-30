from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.title import chunk_by_title
from unstructured.cleaners.core import group_broken_paragraphs, clean
from unstructured.documents.elements import CompositeElement, Table, TableChunk
from typing import List, Dict, Any, Optional
import os
import re
from tqdm import tqdm

class UnstructuredProcessor():
    """Implementation using Unstructured approach"""

    def __init__(self):
        self.default_settings = {
            'remove_header_footer': {'enabled': True, 'header_regex': '', 'footer_regex': ''},
            'extract_tables_images': {'enabled': True, 'images_path': None},
            'remove_matches': {'enabled': False, 'regex_patterns': ['']},
            'split_paragraphs': {'enabled': True},
            'split_chunk': {'enabled': True, 'max_characters': 512, 'overlap': 30},
            'sentence_cleaner': {'enabled': True}
        }

    def _sentence_cleaner(self, chunks):
        cleaned_chunks = []
        for chunk in chunks:
            if chunk.category not in ['Table', 'TableChunk']:
                cleaned_text = chunk.text.strip("\n").strip()
            else:
                cleaned_text = chunk.text
            if len(cleaned_text) >= 10:
                metadata=chunk.metadata.to_dict()
                cleaned_chunks.append({
                     'document_title': metadata.get('filename'),
                     'document_page': metadata.get('page_number'),
                     'text': cleaned_text,
                     'n_tokens': len(cleaned_text.split())
                 })
        return cleaned_chunks

    def _split_paragraphs(self, chunks):
        split_chunks = []
        for chunk in chunks:
            if not isinstance(chunk, (Table, TableChunk)):
                paragraphs = chunk.text.split("\n\n")
            else:
                paragraphs = [chunk.text]
            for paragraph in paragraphs:
                cleaned_paragraph = paragraph.strip()
                metadata = chunk.metadata
                split_chunk = CompositeElement(
                    text=cleaned_paragraph,
                    metadata=metadata
                )
                split_chunks.append(split_chunk)
        return split_chunks
    
    def process_files(self, pdf_files: List[str], settings: Dict[str, Any] = None) -> List[Dict]:
        # Merge default settings with provided settings
        settings = {**self.default_settings, **(settings or {})}
        
        chunks = []
        for filepath in tqdm(pdf_files):
            try:
                # PDF partitioning, export images
                pdf_manager = partition_pdf(
                    filepath, 
                    strategy="hi_res",
                    infer_table_structure=True,
                    extract_images_in_pdf=True,
                    extract_image_block_types=["Image", "Table"],
                    extract_image_block_output_dir=settings['extract_tables_images']['images_path']
                )
                
                # Remove automatically header and footer
                if settings['remove_header_footer']['enabled']:
                    pdf_manager = [el for el in pdf_manager if el.category not in ["Header", "Footer"]]
                
                # Chunk by section
                text_chunks = chunk_by_title(
                    pdf_manager,
                    overlap=settings['split_chunk']['overlap'],
                    max_characters=settings['split_chunk']['max_characters']
                )
                
                # Remove matches if specified
                if settings['remove_matches']['enabled']:
                    for i, chunk in enumerate(text_chunks):
                        for regex_pattern in settings['remove_matches']['regex_patterns']:
                            text_chunks[i].text = re.sub(regex_pattern, "", chunk.text)

                # Sentence Cleaner
                if settings['sentence_cleaner']['enabled']:
                    for i, chunk in enumerate(text_chunks):
                        cleaned_text = clean(chunk.text, bullets=True, extra_whitespace=True, dashes=True)
                        text_chunks[i].text = cleaned_text

                # Paragraph Splitter
                if settings['split_paragraphs']['enabled']:
                    text_chunks = self._split_paragraphs(text_chunks)

                # Convert to common chunk format
                for chunk in text_chunks:
                    metadata = {
                        'document_page': chunk.metadata.page_number,
                        'category': chunk.category,
                    }
                    
                    # Add text_as_html only for tables
                    if chunk.category in ['Table', 'TableChunk']:
                        metadata['text_as_html'] = chunk.metadata.text_as_html
                    
                    chunks.append({
                        'document_title': chunk.metadata.filename,
                        'text': chunk.metadata.text_as_html if chunk.category in ['Table', 'TableChunk'] else chunk.text,
                        'n_tokens': len(chunk.text.split()),
                        'document_page': chunk.metadata.page_number,
                        'category': chunk.category,
                    })
                       
            except Exception as e:
                print(f"Error procesando: '{os.path.basename(filepath)}': {e}")
                
        for i, chunk in enumerate(chunks):
            chunk['chunk_id'] = i
            chunk['document_id'] = hash(chunk['document_title']) % (10 ** 8)
        return chunks