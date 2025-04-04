# Milvus Implementations

This folder contains two implementations for working with Milvus vector database for Retrieval Augmented Generation (RAG) applications.

## Milvus_snippets.py

`Milvus_snippets.py` is a notebook-style implementation that demonstrates a complete end-to-end workflow for:

- Processing documents (PDF, Markdown)
- Generating embeddings using watsonx.ai
- Storing vectors in Milvus
- Performing semantic search
- Implementing additional techniques:
  - Reranking results
  - Using reflection to evaluate chunk relevance

This implementation is ideal for learning and experimenting with RAG concepts.

## MilvusClient.py

`MilvusClient.py` is a more structured, production-ready implementation that offers:

- Object-oriented design with the Singleton pattern
- Comprehensive search capabilities:
  - Dense vector search using embeddings
  - Sparse vector search using BM25
  - Hybrid search combining both approaches with configurable reranking
- Robust error handling and logging
- Collection management utilities
- Schema and index creation helpers

This implementation is designed to be integrated into larger applications as a component.

## Usage Guidance

- For exploration, learning, and prototyping, start with `Milvus_snippets.py`
- For production applications, use `MilvusClient.py`

Both implementations are functional and demonstrate integration with watsonx.ai for embeddings and foundation models. MilvusClient is a newer version that takes advantage of Milvus's more advanced capabilities for sparse, dense, and hybrid search with reranking.