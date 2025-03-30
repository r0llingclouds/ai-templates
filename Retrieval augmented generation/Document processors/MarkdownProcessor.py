import re
from typing import List, Dict
from pathlib import Path
from transformers import AutoTokenizer

class MarkdownProcessor:
    def __init__(self, max_tokens: int = 512):
        self.max_tokens = max_tokens
        self.tokenizer = AutoTokenizer.from_pretrained("fxmarty/tiny-llama-fast-tokenizer")

    def _split_text_into_subblocks(self, text: str) -> List[str]:
        sentences = re.split(r'(?<=[.!?]) +', text)
        subblocks = []
        current_subblock = ''
        current_tokens = 0

        for sentence in sentences:
            sentence_tokens = len(self.tokenizer.encode(sentence))
            
            if sentence_tokens > self.max_tokens:
                words = sentence.split()
                word_tokens = [len(self.tokenizer.encode(word)) for word in words]
                current_sentence = ''
                current_sentence_tokens = 0
                
                for word, word_token_count in zip(words, word_tokens):
                    if current_sentence_tokens + word_token_count > self.max_tokens:
                        subblocks.append(current_sentence.strip())
                        current_sentence = word
                        current_sentence_tokens = word_token_count
                    else:
                        current_sentence += ' ' + word
                        current_sentence_tokens += word_token_count
                        
                if current_sentence.strip():
                    subblocks.append(current_sentence.strip())
            else:
                if current_tokens + sentence_tokens > self.max_tokens:
                    if current_subblock:
                        subblocks.append(current_subblock.strip())
                    current_subblock = sentence
                    current_tokens = sentence_tokens
                else:
                    current_subblock += ' ' + sentence
                    current_tokens += sentence_tokens

        if current_subblock.strip():
            subblocks.append(current_subblock.strip())

        return subblocks

    def _process_single_file(self, markdown_text: str, filename: str) -> List[Dict]:
        # Use the provided filename as the document title
        doc_title = filename
        # Generate document_id using hash
        doc_id = hash(doc_title) % (10 ** 8)
        
        blocks = re.split(r'(\n\s*\n)', markdown_text)
        blocks = [block for block in blocks if block.strip() != '' and not block.isspace()]
        
        chunks = []
        current_chunk = ''
        current_tokens = 0
        chunk_counter = 0  # Initialize chunk counter for this document
        
        for block in blocks:
            block_tokens = len(self.tokenizer.encode(block))
            
            if block_tokens > self.max_tokens:
                subblocks = self._split_text_into_subblocks(block)
                for subblock in subblocks:
                    subblock_tokens = len(self.tokenizer.encode(subblock))
                    if current_tokens + subblock_tokens > self.max_tokens:
                        if current_chunk:
                            chunks.append({
                                'document_title': doc_title,
                                'document_id': doc_id,
                                'chunk_id': chunk_counter,
                                'text': current_chunk.strip(),
                                'n_tokens': current_tokens
                            })
                            chunk_counter += 1
                        current_chunk = subblock
                        current_tokens = subblock_tokens
                    else:
                        current_chunk += ' ' + subblock
                        current_tokens += subblock_tokens
            else:
                if current_tokens + block_tokens > self.max_tokens:
                    if current_chunk:
                        chunks.append({
                            'document_title': doc_title,
                            'document_id': doc_id,
                            'chunk_id': chunk_counter,
                            'text': current_chunk.strip(),
                            'n_tokens': current_tokens
                        })
                        chunk_counter += 1
                    current_chunk = block
                    current_tokens = block_tokens
                else:
                    current_chunk += '\n' + block
                    current_tokens += block_tokens
        
        if current_chunk.strip():
            chunks.append({
                'document_title': doc_title,
                'document_id': doc_id,
                'chunk_id': chunk_counter,
                'text': current_chunk.strip(),
                'n_tokens': current_tokens
            })
        
        return chunks

    def process_files(self, file_contents: Dict[str, str]) -> List[Dict]:
        """
        Process multiple markdown files from a dictionary of file contents.
        
        Args:
            file_contents: Dictionary mapping filenames (without extension) to their contents
            
        Returns:
            List of dictionaries containing chunks with their metadata including:
                - document_title: Original filename
                - document_id: Hash of document_title modulo 10^8
                - chunk_id: Sequential ID for each chunk within a document
                - text: The chunk content
                - n_tokens: Number of tokens in the chunk
        """
        all_chunks = []
        
        for filename, content in file_contents.items():
            try:
                all_chunks.extend(self._process_single_file(content, filename))
            except Exception as e:
                print(f"Error processing file {filename}: {str(e)}")
                
        return all_chunks