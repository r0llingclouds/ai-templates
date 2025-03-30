ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_extensions_rag.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# RAG [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#rag "Link to this heading")

Note

Added in 1.1.x release

## Chunkers [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#chunkers "Link to this heading")

### LangChainChunker [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#langchainchunker "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.chunker.langchain\_chunker.LangChainChunker( _method='recursive'_, _chunk\_size=4000_, _chunk\_overlap=200_, _encoding\_name='gpt2'_, _model\_name=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/langchain_chunker.html#LangChainChunker) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.langchain_chunker.LangChainChunker "Link to this definition")

Bases: [`BaseChunker`](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.base_chunker.BaseChunker "ibm_watsonx_ai.foundation_models.extensions.rag.chunker.base_chunker.BaseChunker")\[ `Document`\]

Wrapper for LangChain TextSplitter.

Parameters:

- **method** ( _Literal_ _\[_ _"recursive"_ _,_ _"character"_ _,_ _"token"_ _\]_ _,_ _optional_) – describes the type of TextSplitter as the main instance performing the chunking, defaults to “recursive”

- **chunk\_size** ( _int_ _,_ _optional_) – maximum size of a single chunk that is returned, defaults to 4000

- **chunk\_overlap** ( _int_ _,_ _optional_) – overlap in characters between chunks, defaults to 200

- **encoding\_name** ( _str_ _,_ _optional_) – encoding used in the TokenTextSplitter, defaults to “gpt2”

- **model\_name** ( _str_ _,_ _optional_) – model used in the TokenTextSplitter


```
from ibm_watsonx_ai.foundation_models.extensions.rag.chunker import LangChainChunker

text_splitter = LangChainChunker(
    method="recursive",
    chunk_size=1000,
    chunk_overlap=200
)

chunks_ids = []

for i, document in enumerate(data_loader):
    chunks = text_splitter.split_documents([document])
    chunks_ids.append(vector_store.add_documents(chunks, batch_size=300))

```

_classmethod_ from\_dict( _d_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/langchain_chunker.html#LangChainChunker.from_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.langchain_chunker.LangChainChunker.from_dict "Link to this definition")

Create an instance from the dictionary.

split\_documents( _documents_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/langchain_chunker.html#LangChainChunker.split_documents) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.langchain_chunker.LangChainChunker.split_documents "Link to this definition")

Split series of documents into smaller chunks based on the provided
chunker settings. Each chunk has metadata that includes the document\_id,
sequence\_number, and start\_index.

Parameters:

**documents** ( _Sequence_ _\[_ _langchain\_core.documents.Document_ _\]_) – sequence of elements that contain context in a text format

Returns:

list of documents split into smaller ones, having less content

Return type:

list\[langchain\_core.documents.Document\]

supported\_methods _=('recursive','character','token')_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.langchain_chunker.LangChainChunker.supported_methods "Link to this definition")to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/langchain_chunker.html#LangChainChunker.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.langchain_chunker.LangChainChunker.to_dict "Link to this definition")

Return dictionary that can be used to recreate an instance of the LangChainChunker.

### BaseChunker [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#basechunker "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.chunker.base\_chunker.BaseChunker [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/base_chunker.html#BaseChunker) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.base_chunker.BaseChunker "Link to this definition")

Bases: `ABC`, `Generic`\[ `ChunkType`\]

Responsible for handling splitting document operations
in the RAG application.

_abstractclassmethod_ from\_dict( _d_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/base_chunker.html#BaseChunker.from_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.base_chunker.BaseChunker.from_dict "Link to this definition")

Create an instance from the dictionary.

_abstract_ split\_documents( _documents_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/base_chunker.html#BaseChunker.split_documents) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.base_chunker.BaseChunker.split_documents "Link to this definition")

Split series of documents into smaller parts based on
the provided chunker settings.

Parameters:

**documents** – sequence of elements that contain context in a text format

Type:

Sequence\[ChunkType\]

Returns:

list of documents split into smaller ones, having less content

Return type:

list\[ChunkType\]

_abstract_ to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/chunker/base_chunker.html#BaseChunker.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.chunker.base_chunker.BaseChunker.to_dict "Link to this definition")

Return dictionary that can be used to recreate an instance of the BaseChunker.

## Retrievers [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#retrievers "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.retriever.retriever.Retriever( _vector\_store_, _method=RetrievalMethod.SIMPLE_, _window\_size=2_, _number\_of\_chunks=5_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/retriever.html#Retriever) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.Retriever "Link to this definition")

Bases: [`BaseRetriever`](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever "ibm_watsonx_ai.foundation_models.extensions.rag.retriever.base_retriever.BaseRetriever")

Retriever class that handles the retrieval operation for a RAG implementation.
Returns the number\_of\_chunks document segments using the provided method based on a relevant query in the `retrieve` method.

Parameters:

- **vector\_store** ( [_BaseVectorStore_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore")) – VectorStore to use for the retrieval

- **method** ( [_RetrievalMethod_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.RetrievalMethod "ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.RetrievalMethod") _,_ _optional_) – default retrieval method to use when calling retrieve, defaults to RetrievalMethod.SIMPLE

- **number\_of\_chunks** ( _int_ _,_ _optional_) – number of expected document chunks to be returned, defaults to 5


You can create a repeatable retrieval and return the three nearest documents by using a simple proximity search. To do this,
create a VectorStore and then define a Retriever.

```
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models.extensions.rag import VectorStore
from ibm_watsonx_ai.foundation_models.extensions.rag import Retriever, RetrievalMethod
from ibm_watsonx_ai.foundation_models.embeddings import SentenceTransformerEmbeddings

api_client = APIClient(credentials)

vector_store = VectorStore(
        api_client,
        connection_id='***',
        params={
            'index_name': 'my_test_index',
        },
        embeddings=SentenceTransformerEmbeddings('sentence-transformers/all-MiniLM-L6-v2')
    )

retriever = Retriever(vector_store=vector_store, method=RetrievalMethod.SIMPLE, number_of_chunks=3)

retriever.retrieve("What is IBM known for?")

```

_classmethod_ from\_vector\_store( _vector\_store_, _init\_parameters=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/retriever.html#Retriever.from_vector_store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.Retriever.from_vector_store "Link to this definition")

Deserializes the `init_parameters` retriever into a concrete one using arguments.

Parameters:

- **vector\_store** ( [_BaseVectorStore_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore")) – vector store used to create the retriever

- **init\_parameters** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_) – parameters to initialize the retriever with


Returns:

concrete Retriever or None if data is incorrect

Return type:

[BaseRetriever](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever "ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever") \| None

retrieve( _query_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/retriever.html#Retriever.retrieve) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.Retriever.retrieve "Link to this definition")

Retrieve elements from the VectorStore by using the provided query.

Parameters:

**query** ( _str_) – text query to be used for searching

Returns:

list of retrieved LangChain documents

Return type:

list\[langchain\_core.documents.Document\]

to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/retriever.html#Retriever.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.Retriever.to_dict "Link to this definition")

Serializes the `init_parameters` retriever so it can be reconstructed by the `from_vector_store` class method.

Returns:

serialized `init_parameters`

Return type:

dict

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.retriever.retriever.RetrievalMethod( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/retriever.html#RetrievalMethod) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.RetrievalMethod "Link to this definition")

Bases: `str`, `Enum`

An enumeration.

SIMPLE _='simple'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.RetrievalMethod.SIMPLE "Link to this definition")WINDOW _='window'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.RetrievalMethod.WINDOW "Link to this definition")_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.retriever.retriever.BaseRetriever( _vector\_store_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/base_retriever.html#BaseRetriever) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever "Link to this definition")

Bases: `ABC`

Abstract class for all retriever handlers for the chosen vector store.
Returns some document chunks in a RAG pipeline using a concrete `retrieve` implementation.

Parameters:

**vector\_store** ( [_BaseVectorStore_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore")) – vector store used in document retrieval

_abstractclassmethod_ from\_vector\_store( _vector\_store_, _init\_parameters=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/base_retriever.html#BaseRetriever.from_vector_store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever.from_vector_store "Link to this definition")

Deserializes the `init_parameters` retriever into a concrete one using arguments.

Parameters:

- **vector\_store** ( [_BaseVectorStore_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore")) – vector store used to create the retriever

- **init\_parameters** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_) – parameters to initialize the retriever with


Returns:

concrete Retriever or None if data is incorrect

Return type:

[BaseRetriever](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever "ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever") \| None

_abstract_ retrieve( _query_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/base_retriever.html#BaseRetriever.retrieve) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever.retrieve "Link to this definition")

Retrieve elements from the vector store using the provided query.

Parameters:

**query** ( _str_) – text query to be used for searching

Returns:

list of retrieved LangChain documents

Return type:

list\[langchain\_core.documents.Document\]

to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/retriever/base_retriever.html#BaseRetriever.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.retriever.retriever.BaseRetriever.to_dict "Link to this definition")

Serializes the `init_parameters` retriever so it can be reconstructed by the `from_vector_store` class method.

Returns:

serialized `init_parameters`

Return type:

dict

## Vector Stores [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#vector-stores "Link to this heading")

### VectorStore [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#vectorstore "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.vector\_stores.vector\_store.VectorStore( _api\_client=None_, _\*_, _connection\_id=None_, _embeddings=None_, _index\_name=None_, _datasource\_type=None_, _distance\_metric=None_, _langchain\_vector\_store=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore "Link to this definition")

Bases: [`BaseVectorStore`](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore")

Universal vector store client for a RAG pattern.

Instantiates the vector store connection in the Watson Machine Learning environment and handles the necessary operations.
The parameters given by the keyword arguments are used to instantiate the vector store client in their
particular constructor. Those parameters might be parsed differently.

For details, refer to the VectorStoreConnector `get_...` methods.

You can utilize the custom embedding function. This function can be provided in the constructor or by the `set_embeddings` method.
For available embeddings, refer to the `ibm_watsonx_ai.foundation_models.embeddings` module.

Parameters:

- **api\_client** ( [_APIClient_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "client.APIClient") _,_ _optional_) – WatsonX API client required if connecting by connection\_id, defaults to None

- **connection\_id** ( _str_ _,_ _optional_) – connection asset ID, defaults to None

- **embeddings** ( [_BaseEmbeddings_](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings "ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings") _,_ _optional_) – default embeddings to be used, defaults to None

- **index\_name** ( _str_ _,_ _optional_) – name of the vector database index, defaults to None

- **datasource\_type** ( [_VectorStoreDataSourceType_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType") _,_ _str_ _,_ _optional_) – data source type to use when `connection_id` is not provided, keyword arguments will be used to establish connection, defaults to None

- **distance\_metric** ( _Literal_ _\[_ _"euclidean"_ _,_ _"cosine"_ _\]_ _,_ _optional_) – metric used for determining vector distance, defaults to None

- **langchain\_vector\_store** ( [_VectorStore_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore") _,_ _optional_) – use LangChain vector store, defaults to None


**Example:**

To connect, provide the connection asset ID.
You can use custom embeddings to add and search documents.

```
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models.extensions.rag import VectorStore
from ibm_watsonx_ai.foundation_models.embeddings import SentenceTransformerEmbeddings

api_client = APIClient(credentials)

 embedding = Embeddings(
         model_id=EmbeddingTypes.IBM_SLATE_30M_ENG,
         api_client=api_client
         )

vector_store = VectorStore(
        api_client,
        connection_id='***',
        index_name='my_test_index',
        embeddings=embedding
    )

vector_store.add_documents([\
    {'content': 'document one content', 'metadata':{'url':'ibm.com'}},\
    {'content': 'document two content', 'metadata':{'url':'ibm.com'}}\
])

vector_store.search('one', k=1)

```

Note

Optionally, like in LangChain, it is possible to use a cloud ID and API key parameters to connect to Elastic Cloud.
The keyword arguments can be used as direct params to LangChain’s `ElasticsearchStore` constructor.

```
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models.extensions.rag import VectorStore

api_client = APIClient(credentials)

vector_store = VectorStore(
        api_client,
        index_name='my_test_index',
        model_id=".elser_model_2_linux-x86_64",
        cloud_id='***',
        api_key=IAM_API_KEY
    )

vector_store.add_documents([\
    {'content': 'document one content', 'metadata':{'url':'ibm.com'}},\
    {'content': 'document two content', 'metadata':{'url':'ibm.com'}}\
])

vector_store.search('one', k=1)

```

add\_documents( _content_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.add_documents) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.add_documents "Link to this definition")

Adds a list of documents to the RAG’s vector store as an upsert operation.
IDs are determined by the text content of the document (hash). Duplicates will not be added.

The list must contain strings, dictionaries with a required `content` field of a string type, or a LangChain `Document`.

Parameters:

**content** ( _list_ _\[_ _str_ _\]_ _\|_ _list_ _\[_ _dict_ _\]_ _\|_ _list_) – unstructured list of data to be added

Returns:

list of IDs

Return type:

list\[str\]

_async_ add\_documents\_async( _content_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.add_documents_async) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.add_documents_async "Link to this definition")

Add document to the RAG’s vector store asynchronously.
The list must contain strings, dictionaries with a required `content` field of a string type, or a LangChain `Document`.

Parameters:

**content** ( _list_ _\[_ _str_ _\]_ _\|_ _list_ _\[_ _dict_ _\]_ _\|_ _list_) – unstructured list of data to be added

Returns:

list of IDs

Return type:

list\[str\]

as\_langchain\_retriever( _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.as_langchain_retriever) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.as_langchain_retriever "Link to this definition")

Creates a LangChain retriever from this vector store.

Returns:

LangChain retriever that can be used in LangChain pipelines

Return type:

langchain\_core.vectorstores.VectorStoreRetriever

clear() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.clear) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.clear "Link to this definition")

Clears the current collection that is being used by the vector store.
Removes all documents with all their metadata and embeddings.

count() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.count) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.count "Link to this definition")

Returns the number of documents in the current collection.

Returns:

number of documents in the collection

Return type:

int

delete( _ids_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.delete "Link to this definition")

Delete documents with provided IDs.

Parameters:

**ids** ( _list_ _\[_ _str_ _\]_) – IDs of documents to be deleted

_classmethod_ from\_dict( _client=None_, _data=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.from_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.from_dict "Link to this definition")

Creates `VectorStore` using only a primitive data type dict.

Parameters:

**data** ( _dict_) – dict in schema like the `to_dict()` method

Returns:

reconstructed VectorStore

Return type:

[VectorStore](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore")

get\_client() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.get_client) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.get_client "Link to this definition")

Returns an underlying native vector store client.

Returns:

wrapped vector store client

Return type:

Any

search( _query_, _k_, _include\_scores=False_, _verbose=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.search) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.search "Link to this definition")

Searches for documents most similar to the query.

The method is designed as a wrapper for respective LangChain VectorStores’ similarity search methods.
Therefore, additional search parameters passed in `kwargs` should be consistent with those methods,
and can be found in the LangChain documentation as they may differ depending on the connection
type: Milvus, Chroma, Elasticsearch, etc.

Parameters:

- **query** ( _str_) – text query

- **k** ( _int_) – number of documents to retrieve

- **include\_scores** ( _bool_) – whether similarity scores of found documents should be returned, defaults to False

- **verbose** ( _bool_) – whether to display a table with the found documents, defaults to False


Returns:

list of found documents

Return type:

list

set\_embeddings( _embedding\_fn_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.set_embeddings) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.set_embeddings "Link to this definition")

If possible, sets a default embedding function.
To make the function capable for a `RAGPattern` deployment, use types inherited from `BaseEmbeddings`.
The `embedding_fn` argument can be a LangChain embedding but issues with serialization will occur.

_Deprecated:_ The set\_embeddings method for the VectorStore class is deprecated, because it might cause issues for ‘langchain >= 0.2.0’.

Parameters:

**embedding\_fn** ( [_BaseEmbeddings_](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings "ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings")) – embedding function

to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.to_dict "Link to this definition")

Serialize `VectorStore` into a dict that allows reconstruction using the `from_dict` class method.

Returns:

dict for the from\_dict initialization

Return type:

dict

window\_search( _query_, _k_, _include\_scores=False_, _verbose=False_, _window\_size=2_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store.html#VectorStore.window_search) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store.VectorStore.window_search "Link to this definition")

Similarly to the search method, gets documents (chunks) that would fit the query.
Each chunk is extended to its adjacent chunks (if they exist) from the same origin document.
The adjacent chunks are merged into one chunk while keeping their order,
and any intersecting text between them is merged (if it exists).
This requires chunks to have “document\_id” and “sequence\_number” in their metadata.

Parameters:

- **query** ( _str_) – question asked by a user

- **k** ( _int_) – maximum number of similar documents

- **include\_scores** ( _bool_ _,_ _optional_) – return scores for documents, defaults to False

- **verbose** ( _bool_ _,_ _optional_) – print formatted response to the output, defaults to False

- **window\_size** ( _int_) – number of adjacent chunks to retrieve before and after the center, according to the sequence\_number.


Returns:

list of found documents (extended into windows).

Return type:

list

### BaseVectorStore [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#basevectorstore "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.vector\_stores.base\_vector\_store.BaseVectorStore [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "Link to this definition")

Bases: `ABC`

Base abstract class for all vector store-like classes. Interface that supports simple database operations.

_abstract_ add\_documents( _content_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.add_documents) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.add_documents "Link to this definition")

Adds a list of documents to the RAG’s vector store as an upsert operation.
IDs are determined by the text content of the document (hash). Duplicates will not be added.

The list must contain strings, dictionaries with a required `content` field of a string type, or a LangChain `Document`.

Parameters:

**content** ( _list_ _\[_ _str_ _\]_ _\|_ _list_ _\[_ _dict_ _\]_ _\|_ _list_) – unstructured list of data to be added

Returns:

list of IDs

Return type:

list\[str\]

_abstractasync_ add\_documents\_async( _content_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.add_documents_async) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.add_documents_async "Link to this definition")

Add document to the RAG’s vector store asynchronously.
The list must contain strings, dictionaries with a required `content` field of a string type, or a LangChain `Document`.

Parameters:

**content** ( _list_ _\[_ _str_ _\]_ _\|_ _list_ _\[_ _dict_ _\]_ _\|_ _list_) – unstructured list of data to be added

Returns:

list of IDs

Return type:

list\[str\]

_abstract_ as\_langchain\_retriever( _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.as_langchain_retriever) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.as_langchain_retriever "Link to this definition")

Creates a LangChain retriever from this vector store.

Returns:

LangChain retriever that can be used in LangChain pipelines

Return type:

langchain\_core.vectorstores.VectorStoreRetriever

_abstract_ clear() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.clear) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.clear "Link to this definition")

Clears the current collection that is being used by the vector store.
Removes all documents with all their metadata and embeddings.

_abstract_ count() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.count) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.count "Link to this definition")

Returns the number of documents in the current collection.

Returns:

number of documents in the collection

Return type:

int

_abstract_ delete( _ids_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.delete "Link to this definition")

Delete documents with provided IDs.

Parameters:

**ids** ( _list_ _\[_ _str_ _\]_) – IDs of documents to be deleted

_abstract_ get\_client() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.get_client) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.get_client "Link to this definition")

Returns an underlying native vector store client.

Returns:

wrapped vector store client

Return type:

Any

_abstract_ search( _query_, _k_, _include\_scores=False_, _verbose=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.search) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.search "Link to this definition")

Get documents that would fit the query.

Parameters:

- **query** ( _str_) – question asked by a user

- **k** ( _int_) – maximum number of similar documents

- **include\_scores** ( _bool_ _,_ _optional_) – return scores for documents, defaults to False

- **verbose** ( _bool_ _,_ _optional_) – print formatted response to the output, defaults to False


Returns:

list of found documents

Return type:

list

_abstract_ set\_embeddings( _embedding\_fn_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.set_embeddings) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.set_embeddings "Link to this definition")

If possible, sets a default embedding function.
To make the function capable for a `RAGPattern` deployment, use types inherited from `BaseEmbeddings`.
The `embedding_fn` argument can be a LangChain embedding but issues with serialization will occur.

_Deprecated:_ The set\_embeddings method for the VectorStore class is deprecated, because it might cause issues for ‘langchain >= 0.2.0’.

Parameters:

**embedding\_fn** ( [_BaseEmbeddings_](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings "ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings")) – embedding function

_abstract_ window\_search( _query_, _k_, _include\_scores=False_, _verbose=False_, _window\_size=2_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/base_vector_store.html#BaseVectorStore.window_search) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore.window_search "Link to this definition")

Similarly to the search method, gets documents (chunks) that would fit the query.
Each chunk is extended to its adjacent chunks (if they exist) from the same origin document.
The adjacent chunks are merged into one chunk while keeping their order,
and any intersecting text between them is merged (if it exists).
This requires chunks to have “document\_id” and “sequence\_number” in their metadata.

Parameters:

- **query** ( _str_) – question asked by a user

- **k** ( _int_) – maximum number of similar documents

- **include\_scores** ( _bool_ _,_ _optional_) – return scores for documents, defaults to False

- **verbose** ( _bool_ _,_ _optional_) – print formatted response to the output, defaults to False

- **window\_size** ( _int_) – number of adjacent chunks to retrieve before and after the center, according to the sequence\_number.


Returns:

list of found documents (extended into windows).

Return type:

list

### VectorStoreConnector [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#vectorstoreconnector "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.vector\_stores.vector\_store\_connector.VectorStoreConnector( _properties=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreConnector) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreConnector "Link to this definition")

Bases: `object`

Creates a proper vector store client using the provided properties.

Properties are arguments to the LangChain vector stores of a desired type.
Also parses properties extracted from connection assets into one that would fit for initialization.

Custom or connection asset properties that are parsed are:
\\* index\_name
\\* distance\_metric
\\* username
\\* password
\\* ssl\_certificate
\\* embeddings

Parameters:

**properties** ( _dict_) – dictionary with all the required key values to establish the connection

get\_chroma() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreConnector.get_chroma) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreConnector.get_chroma "Link to this definition")

Creates an in-memory vector store for Chroma.

Raises:

**ImportError** – langchain required

Returns:

vector store adapter for LangChain’s Chroma

Return type:

[LangChainVectorStoreAdapter](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter")

get\_elasticsearch() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreConnector.get_elasticsearch) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreConnector.get_elasticsearch "Link to this definition")

Creates an Elasticsearch vector store.

Raises:

**ImportError** – langchain required

Returns:

vector store adapter for LangChain’s Elasticsearch

Return type:

[LangChainVectorStoreAdapter](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter")

get\_from\_type( _type_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreConnector.get_from_type) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreConnector.get_from_type "Link to this definition")

Gets a vector store based on the provided type (matching from DataSource names from SDK API).

Parameters:

**type** ( [_VectorStoreDataSourceType_](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType")) – DataSource type string from SDK API

Raises:

**TypeError** – unsupported type

Returns:

proper BaseVectorStore type constructed from properties

Return type:

[BaseVectorStore](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore")

get\_langchain\_adapter( _langchain\_vector\_store_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreConnector.get_langchain_adapter) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreConnector.get_langchain_adapter "Link to this definition")

Creates an adapter for a concrete vector store from LangChain.

Parameters:

**langchain\_vector\_store** ( _Any_) – object that is a subclass of the LangChain vector store

Raises:

**ImportError** – LangChain required

Returns:

proper adapter for the vector store

Return type:

[LangChainVectorStoreAdapter](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter")

get\_milvus() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreConnector.get_milvus) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreConnector.get_milvus "Link to this definition")

Creates a Milvus vector store.

Raises:

**ImportError** – langchain required

Returns:

vector store adapter for LangChain’s Milvus

Return type:

[LangChainVectorStoreAdapter](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter")

_static_ get\_type\_from\_langchain\_vector\_store( _langchain\_vector\_store_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreConnector.get_type_from_langchain_vector_store) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreConnector.get_type_from_langchain_vector_store "Link to this definition")

Returns `DataSourceType` for concrete LangChain `VectorStore` class.

Parameters:

**langchain\_vector\_store** ( _Any_) – vector store object from LangChain

Returns:

DataSourceType name

Return type:

[VectorStoreDataSourceType](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType")

### VectorStoreDataSourceType [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#vectorstoredatasourcetype "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.vector\_stores.vector\_store\_connector.VectorStoreDataSourceType( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/vector_store_connector.html#VectorStoreDataSourceType) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType "Link to this definition")

Bases: `str`, `Enum`

An enumeration.

CHROMA _='chroma'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType.CHROMA "Link to this definition")ELASTICSEARCH _='elasticsearch'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType.ELASTICSEARCH "Link to this definition")MILVUS _='milvus'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType.MILVUS "Link to this definition")MILVUS\_WXD _='milvuswxd'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType.MILVUS_WXD "Link to this definition")UNDEFINED _='undefined'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.vector_store_connector.VectorStoreDataSourceType.UNDEFINED "Link to this definition")

### LangChainVectorStoreAdapter [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html\#langchainvectorstoreadapter "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extensions.rag.vector\_stores.langchain\_vector\_store\_adapter.LangChainVectorStoreAdapter( _vector\_store_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter "Link to this definition")

Bases: [`BaseVectorStore`](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore "ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.base_vector_store.BaseVectorStore")

Adapter for LangChain `VectorStore` base class.

Parameters:

**vector\_store** ( _langchain\_core.vectorstore.VectorStore_) – concrete LangChain vector store object

add\_documents( _content_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.add_documents) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.add_documents "Link to this definition")

Adds a list of documents to the RAG’s vector store as an upsert operation.
IDs are determined by the text content of the document (hash). Duplicates will not be added.

The list must contain strings, dictionaries with a required `content` field of a string type, or a LangChain `Document`.

Parameters:

**content** ( _list_ _\[_ _str_ _\]_ _\|_ _list_ _\[_ _dict_ _\]_ _\|_ _list_) – unstructured list of data to be added

Returns:

list of IDs

Return type:

list\[str\]

_async_ add\_documents\_async( _content_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.add_documents_async) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.add_documents_async "Link to this definition")

Add document to the RAG’s vector store asynchronously.
The list must contain strings, dictionaries with a required `content` field of a string type, or a LangChain `Document`.

Parameters:

**content** ( _list_ _\[_ _str_ _\]_ _\|_ _list_ _\[_ _dict_ _\]_ _\|_ _list_) – unstructured list of data to be added

Returns:

list of IDs

Return type:

list\[str\]

as\_langchain\_retriever( _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.as_langchain_retriever) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.as_langchain_retriever "Link to this definition")

Creates a LangChain retriever from this vector store.

Returns:

LangChain retriever that can be used in LangChain pipelines

Return type:

langchain\_core.vectorstores.VectorStoreRetriever

clear() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.clear) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.clear "Link to this definition")

Clears the current collection that is being used by the vector store.
Removes all documents with all their metadata and embeddings.

count() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.count) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.count "Link to this definition")

Returns the number of documents in the current collection.

Returns:

number of documents in the collection

Return type:

int

delete( _ids_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.delete) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.delete "Link to this definition")

Delete documents with provided IDs.

Parameters:

**ids** ( _list_ _\[_ _str_ _\]_) – IDs of documents to be deleted

get\_client() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.get_client) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.get_client "Link to this definition")

Returns an underlying native vector store client.

Returns:

wrapped vector store client

Return type:

Any

search( _query_, _k_, _include\_scores=False_, _verbose=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.search) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.search "Link to this definition")

Get documents that would fit the query.

Parameters:

- **query** ( _str_) – question asked by a user

- **k** ( _int_) – maximum number of similar documents

- **include\_scores** ( _bool_ _,_ _optional_) – return scores for documents, defaults to False

- **verbose** ( _bool_ _,_ _optional_) – print formatted response to the output, defaults to False


Returns:

list of found documents

Return type:

list

set\_embeddings( _embedding\_fn_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.set_embeddings) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.set_embeddings "Link to this definition")

If possible, sets a default embedding function.
To make the function capable for a `RAGPattern` deployment, use types inherited from `BaseEmbeddings`.
The `embedding_fn` argument can be a LangChain embedding but issues with serialization will occur.

_Deprecated:_ The set\_embeddings method for the VectorStore class is deprecated, because it might cause issues for ‘langchain >= 0.2.0’.

Parameters:

**embedding\_fn** ( [_BaseEmbeddings_](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings "ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings")) – embedding function

window\_search( _query_, _k_, _include\_scores=False_, _verbose=False_, _window\_size=2_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extensions/rag/vector_stores/langchain_vector_store_adapter.html#LangChainVectorStoreAdapter.window_search) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_rag.html#ibm_watsonx_ai.foundation_models.extensions.rag.vector_stores.langchain_vector_store_adapter.LangChainVectorStoreAdapter.window_search "Link to this definition")

Similarly to the search method, gets documents (chunks) that would fit the query.
Each chunk is extended to its adjacent chunks (if they exist) from the same origin document.
The adjacent chunks are merged into one chunk while keeping their order,
and any intersecting text between them is merged (if it exists).
This requires chunks to have “document\_id” and “sequence\_number” in their metadata.

Parameters:

- **query** ( _str_) – question asked by a user

- **k** ( _int_) – maximum number of similar documents

- **include\_scores** ( _bool_ _,_ _optional_) – return scores for documents, defaults to False

- **verbose** ( _bool_ _,_ _optional_) – print formatted response to the output, defaults to False

- **window\_size** ( _int_) – number of adjacent chunks to retrieve before and after the center, according to the sequence\_number.


Returns:

list of found documents (extended into windows).

Return type:

list