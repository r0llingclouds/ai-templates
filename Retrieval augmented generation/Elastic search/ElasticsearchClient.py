from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from aeat_code_rag_backend.Logger import Logger
from aeat_code_rag_backend.env import LogConfig, ElasticsearchConfig, EmbeddingsConfig
from aeat_code_rag_backend.connectors.Singleton import Singleton
from aeat_code_rag_backend.connectors.EmbeddingsClient import EmbeddingClient




class ElasticsearchClient(metaclass=Singleton):
    """
    ElasticsearchClient is a singleton class that provides a client for Elasticsearch.
    It offers methods to create indices, insert data, and perform dense, sparse, and hybrid searches.
    """

    def __init__(self, config: ElasticsearchConfig, embeddingsconfig: EmbeddingsConfig):
        """Initialize the Elasticsearch client and embeddings client."""
        self.logger = Logger('elasticsearch_logger', LogConfig.misc_level).logger
        self.client = Elasticsearch(hosts=config.hosts)  # Add authentication if needed
        self.logger.debug("Elasticsearch Client successfully initialized.")
        self.embeddings = EmbeddingClient(embeddingsconfig=embeddingsconfig)

    def create_index(self, index_name):
        """Create an Elasticsearch index with a mapping for text and dense vectors."""
        mapping = {
            "mappings": {
                "properties": {
                    "text": {"type": "text"},  # Text field for BM25 search
                    "dense_vector": {
                        "type": "dense_vector",
                        "dims": self.embeddings.dimension  # Dimension from embeddings config
                    }
                }
            }
        }
        try:
            self.client.indices.create(index=index_name, body=mapping)
            self.logger.debug(f"Created index: {index_name}")
        except Exception as e:
            self.logger.error(f"Failed to create index {index_name}: {str(e)}")
            raise

    def prepare_data_for_insertion(self, documents):
        """Prepare documents by generating dense embeddings for insertion."""
        prepared_data = []
        for doc in documents:
            dense_vector = self.embeddings.get_dense_embeddings(doc['text'])
            if dense_vector:
                data_point = {
                    "text": doc['text'],
                    "dense_vector": dense_vector[0]  # Assuming embeddings return a list
                }
                prepared_data.append(data_point)
            else:
                self.logger.warning(f"Failed to generate embedding for document {doc.get('id', 'unknown')}")
        return prepared_data

    def insert_data(self, index_name, prepared_data):
        """Insert prepared data into the specified index using bulk indexing."""
        actions = [{"_index": index_name, "_source": data} for data in prepared_data]
        try:
            success, failed = bulk(self.client, actions)
            self.logger.debug(f"Inserted {success} documents into {index_name}, failed: {failed}")
            return success
        except Exception as e:
            self.logger.error(f"Failed to insert data into {index_name}: {str(e)}")
            raise

    def create_and_load_index(self, index_name, documents):
        """Create an index and load it with documents in one operation."""
        if self.client.indices.exists(index=index_name):
            self.logger.info(f"Index {index_name} already exists, deleting it")
            self.client.indices.delete(index=index_name)
        self.create_index(index_name)
        prepared_data = self.prepare_data_for_insertion(documents)
        result = self.insert_data(index_name, prepared_data)
        return result

    def list_indices(self):
        """List all indices in the Elasticsearch instance."""
        try:
            indices = self.client.indices.get_alias("*").keys()
            self.logger.debug(f"Found {len(indices)} indices")
            return list(indices)
        except Exception as e:
            self.logger.error(f"Failed to list indices: {str(e)}")
            raise

    def get_index_stats(self, index_name):
        """Get statistics and mapping for the specified index."""
        if not self.client.indices.exists(index=index_name):
            raise ValueError(f"Index {index_name} does not exist")
        try:
            stats = self.client.indices.stats(index=index_name)
            mapping = self.client.indices.get_mapping(index=index_name)
            result = {
                "doc_count": stats['_all']['primaries']['docs']['count'],
                "mapping": mapping[index_name]['mappings']
            }
            return result
        except Exception as e:
            self.logger.error(f"Error getting index stats: {str(e)}")
            raise

    def delete_index(self, index_name):
        """Delete the specified index from Elasticsearch."""
        if self.client.indices.exists(index=index_name):
            self.client.indices.delete(index=index_name)
            self.logger.info(f"Index {index_name} deleted")
        else:
            self.logger.warning(f"Index {index_name} does not exist")

    def dense_search(self, index_name, query_text, limit=5, search_type="exact", **kwargs):
        """
        Perform a dense vector search using the query text.

        Args:
            index_name (str): Name of the index to search.
            query_text (str): Text query to generate dense embedding.
            limit (int, optional): Maximum number of results. Defaults to 5.
            search_type (str, optional): Type of search to perform. Options are:
                - "exact": Uses script_score for exact cosine similarity (default).
                - "knn": Uses approximate nearest neighbor search for faster performance.
            **kwargs: Additional parameters for KNN search, such as "num_candidates" (default=100).

        Returns:
            list: List of text strings from the top search results.
        """
        # Generate the query vector from the input text
        query_vector = self.embeddings.get_dense_embeddings(query_text)[0]

        # Choose search method based on search_type
        if search_type == "exact":
            self.logger.debug("Performing exact dense search with script_score")
            query = {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'dense_vector') + 1.0",
                        "params": {"query_vector": query_vector}
                    }
                }
            }
            search_body = {"query": query, "size": limit}
        elif search_type == "knn":
            self.logger.debug("Performing approximate dense search with KNN")
            knn_params = {
                "field": "dense_vector",
                "query_vector": query_vector,
                "k": limit,
                "num_candidates": kwargs.get("num_candidates", 100)
            }
            search_body = {"knn": knn_params}
        else:
            raise ValueError(f"Unknown search_type: {search_type}")

        # Execute the search and return results
        try:
            results = self.client.search(index=index_name, body=search_body)
            hits = results['hits']['hits']
            return [hit['_source']['text'] for hit in hits]
        except Exception as e:
            self.logger.error(f"Dense search failed: {str(e)}")
            raise

    def sparse_search(self, index_name, query_text, limit=5, fuzziness=None):
        """
        Perform a sparse vector search using the query text with optional fuzzy matching.

        Args:
            index_name (str): Name of the index to search.
            query_text (str): Text query for sparse search.
            limit (int, optional): Maximum number of results. Defaults to 5.
            fuzziness (str or int, optional): Fuzziness parameter for fuzzy matching.
                Can be 'AUTO' or an integer (e.g., 1, 2). Defaults to None (no fuzziness).

        Returns:
            list: List of text strings from the top search results.

        Raises:
            ValueError: If fuzziness is provided but is neither 'AUTO' nor an integer.
            Exception: If the Elasticsearch search operation fails.
        """
        # Validate the fuzziness parameter
        if fuzziness is not None and fuzziness != "AUTO" and not isinstance(fuzziness, int):
            raise ValueError("Fuzziness must be None, 'AUTO', or an integer.")

        # Construct the Elasticsearch search query
        search_body = {
            "query": {
                "match": {
                    "text": {
                        "query": query_text
                    }
                }
            },
            "size": limit
        }

        # Add fuzziness to the query if specified
        if fuzziness is not None:
            search_body["query"]["match"]["text"]["fuzziness"] = fuzziness
            self.logger.debug(f"Performing sparse search with fuzziness: {fuzziness}")
        else:
            self.logger.debug("Performing sparse search without fuzziness")

        # Execute the search and process results
        try:
            results = self.client.search(index=index_name, body=search_body)
            hits = results['hits']['hits']
            return [hit['_source']['text'] for hit in hits]
        except Exception as e:
            self.logger.error(f"Sparse search failed: {str(e)}")
            raise

    def hybrid_search(self, index_name, query_text, limit=5, **kwargs):
        """
        Perform a hybrid search combining dense and sparse vector searches using built-in RRF.

        Args:
            index_name (str): Name of the index to search.
            query_text (str): Text query for generating dense embedding and sparse search.
            limit (int, optional): Maximum number of results. Defaults to 5.
            **kwargs: Additional parameters for tuning the search:
                - rank_constant (int, optional): RRF rank constant. Defaults to 60.
                - window_size (int, optional): RRF window size. Defaults to 100.
                - num_candidates (int, optional): Number of candidates for KNN search. Defaults to 100.

        Returns:
            list: List of text strings from the top search results.
        """
        self.logger.debug("Using built-in RRF for hybrid search")

        # Generate dense query vector
        query_vector = self.embeddings.get_dense_embeddings(query_text)[0]

        # Set parameters for built-in RRF and KNN
        rank_constant = kwargs.get("rank_constant", 60)
        window_size = kwargs.get("window_size", 100)
        num_candidates = kwargs.get("num_candidates", 100)

        # Construct the hybrid search query with fuzzy matching
        search_body = {
            "query": {
                "match": {
                    "text": {
                        "query": query_text,
                        "fuzziness": "AUTO",  # Enable fuzzy matching
                        "boost": 1
                    }
                }
            },
            "knn": {
                "field": "dense_vector",
                "query_vector": query_vector,
                "k": limit,
                "num_candidates": num_candidates
            },
            "rank": {
                "rrf": {
                    "rank_constant": rank_constant,
                    "window_size": window_size
                }
            },
            "size": limit
        }

        # Execute the search
        try:
            results = self.client.search(index=index_name, body=search_body)
            hits = results['hits']['hits']
            return [hit['_source']['text'] for hit in hits]
        except Exception as e:
            self.logger.error(f"Built-in RRF hybrid search failed: {str(e)}")
            raise