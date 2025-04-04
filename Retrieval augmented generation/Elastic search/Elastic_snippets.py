# %%
# THIS IS THE PYTHON VERSION OF THE NOTEBOOK FOR USING WITH LLMS
# RAG template for watsonx discovery (Elasticsearch)
# It provices a complete end-to-end example of how to use watsonx discovery to answer questions
# Using watsonx.ai for foundation models and embeddings

# %%
from ibm_watsonx_ai import APIClient, Credentials
import os
credentials = Credentials(
    url = os.getenv("WATSONX_URL"),
    api_key = os.getenv("WATSONX_API_KEY")
)
wx_client = APIClient(credentials)

# %%
# first load all pdf files
path = 'docs'
pdf_files = [os.path.join(path, filename) for filename in os.listdir(path) if filename.lower().endswith('.pdf')]
print(pdf_files)

# %%
# processing pdf files into chunks - option with PDF chunker
# !pip install git+https://$PATIBM@github.ibm.com/tech-garage-spgi/pdf-chunker.git@16cc4c0d793bd11088999a1489e472e463a86077
from PDFChunker import PDFChunker
processor = PDFChunker()
chunks = processor.process_files(pdf_files)

# alternative options for processing pdf files into chunks

# from FitzProcessor import FitzProcessor
# processor = FitzProcessor()
# chunks = processor.process_files(pdf_files)

# from UnstructuredProcessor import UnstructuredProcessor
# processor = UnstructuredProcessor()
# chunks = processor.process_files(pdf_files)

# processing markdown files into chunks with Markdown processor
# path = 'markdown_output'
# markdown_files = [os.path.join(path, filename) for filename in os.listdir(path) if filename.lower().endswith('.md')]
# from MarkdownProcessor import MarkdownProcessor
# processor = MarkdownProcessor(markdown_files, max_chunk_size=512, aggregate_chunks_flag=True)
# chunks = processor.process_files()

# %%
# processing with docling
# it will produce markdown files first
# from docling.document_converter import DocumentConverter
# it can even read webpages
# source = "https://github.com/DS4SD/docling"
# converter = DocumentConverter()
# markdown_files = {} # dict of type filename: file content
# for pdf_file in pdf_files:
#     result = converter.convert(pdf_file)
#     result_output = result.document.export_to_markdown()
#     markdown_files[os.path.basename(pdf_file)] = result_output

# to explore, chunking with docling
# from docling_core.transforms.chunker import HierarchicalChunker
# conv_res = DocumentConverter().convert(source)
# doc = conv_res.document
# chunks = list(HierarchicalChunker().chunk(doc))

# %%
# resulting chunks
import pandas as pd
df = pd.DataFrame(chunks)
df['n_tokens'].hist()

# %%


# %%
# the embedding model that will create embeddings for the questions
from ibm_watsonx_ai.foundation_models import Embeddings
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames as EmbedParams

embed_params = {
    EmbedParams.TRUNCATE_INPUT_TOKENS: 512,
    EmbedParams.RETURN_OPTIONS: {
    'input_text': True
    }
}

embedding_model = Embeddings(
    model_id=wx_client.foundation_models.EmbeddingModels.MULTILINGUAL_E5_LARGE,
    params=embed_params,
    credentials=Credentials(
        api_key=os.getenv("WATSONX_API_KEY"),
        url=os.getenv("WATSONX_URL")
    ),
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

# %%
index_name = "test_index"

# %%
# vanilla embeddings
# you can also use alternatives such as contextual retrieval
import time
from tqdm import tqdm

operations = []
print("Generando embeddings")
start = time.time()
for chunk in tqdm(chunks):
    operations.append({"index": {"_index": index_name}})
    text_to_vectorize = 'query: ' + chunk['text']
    chunk['embedding'] = embedding_model.embed_documents(texts=[text_to_vectorize])[0] # can also use embed_query
    # embedding_model.embed_query(text=description)
    operations.append(chunk)
end = time.time()
execution_time = end - start
print(f"Generando embeddings: {execution_time:.2f} segundos")

# %%


# %%
# connect to elasticsearch
from elasticsearch import Elasticsearch

elastic_client = Elasticsearch(
        os.getenv("ELASTIC_URL"),
        basic_auth=(os.getenv("ELASTIC_USER"), os.getenv("ELASTIC_PASSWORD")),
        verify_certs=False
    )

# Settings for document processing
index_parameters = {
    'mappings': {
        'properties': {
            'chunk_id': {'type': 'integer'},
            'document_id': {'type': 'integer'},
            'document_title': {'type': 'keyword'},
            'document_page': {'type': 'integer'},
            'n_tokens': {'type': 'integer'},
            'text': {'type': 'text'},
            'embedding': {
                'dims': 1024,
                'type': 'dense_vector',
                'similarity': 'cosine',
                'index': True
            }
        }
    }
}

# %%
# delete index if exists (warning!)
elastic_client.indices.delete(index=index_name)

# %%
# optional list indices
indices = [index for index in elastic_client.indices.get_alias(index="*", allow_no_indices=True) if not index.startswith('.')]
print(indices)

# %%
# Create index and populate
elastic_client.indices.create(index=index_name, body=index_parameters)

print("Indexando documentos")
start = time.time()
elastic_client.bulk(index=index_name, operations=operations, refresh=True)
end = time.time()
print(f"Indexación completada en {end - start:.2f} segundos.")

# %%
# list documents in index
def list_documents(index_name: str):
    body = {
            "index": index_name,
            "size": 0,
            "aggs": {
                "titles": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {"document_title": {"terms": {"field": "document_title"}}}
                        ]
                    }
                }
            }
        }

    response = elastic_client.search(**body)
    files = [
        bucket['key']['document_title']
        for bucket in response.body['aggregations']['titles']['buckets']
    ]
    return files

print(list_documents(index_name))

# %%
# if you want to update the index with new documents
if not elastic_client.indices.exists(index=index_name).body:
    raise Exception(f"El índice {index_name} no existe.")

files_in_es = list_documents(index_name)

pdf_files_to_update = [
    os.path.join(path, filename)
    for filename in os.listdir(path)
    if (filename.lower().endswith('.pdf') and os.path.basename(filename) not in files_in_es)
]

if len(pdf_files_to_update) > 0:
    chunks = processor.process_files(pdf_files_to_update)

    operations = []
    print("Generando embeddings")
    start = time.time()
    for chunk in tqdm(chunks):
        operations.append({"index": {"_index": index_name}})
        text_to_vectorize = 'query: ' + chunk['text']
        chunk['embedding'] = embedding_model.embed_documents(texts=[text_to_vectorize])[0]
        operations.append(chunk)
    end = time.time()
    execution_time = end - start
    print(f"Generando embeddings: {execution_time:.2f} segundos")

    print("Indexando documentos")
    start = time.time()
    elastic_client.bulk(index=index_name, operations=operations, refresh=True)
    end = time.time()
    print(f"Indexación completada en {end - start:.2f} segundos.")
else:
    print("No hay nuevos documentos para actualizar el índice.")


# %%
# semantic search
def search(question, index, embedding_model, search_params=None):
    default_search_params = {
            "index": index,
            "knn": {
                "field": "embedding",
                "query_vector": embedding_model.embed_documents(texts=['query: ' + question])[0],
                "k": 10,
                "num_candidates": 100
            }
        }
    search_params = {**default_search_params, **(search_params or {})}

    response = elastic_client.search(**search_params)

    if not response["hits"]["hits"]:
        return None, []

    context = "\n\n\n\n".join(hit["_source"]["text"] for hit in response["hits"]["hits"])

    return context, response['hits']['hits']

# %%
question = "¿Cómo se hace la renovación automática de la póliza blindaje plus?"
context, search_results = search(question, index_name, embedding_model)

# %%
# example of hybrid search including reranking (reciprocal rank fusion)
search_params = {
    "index" : index_name,
    "query": { 
        "bool": {
            "must": {
                "match": {
                    "text": {
                        "query": question,
                        "boost": 1,
                        "fuzziness": "AUTO"
                        }
                }
            }
        }
   },
    "knn": { 
        "field": "embedding",
        "k": 10,
        "num_candidates": 100,
        "query_vector": embedding_model.embed_documents(texts=[question])[0]
    },
    "rank": {
        "rrf": {
            "rank_constant": 60,
            "window_size":  100
        }
    },
   "size": 5
}

# %%


# %%
from ibm_watsonx_ai import APIClient, Credentials
credentials = Credentials(
    url = os.getenv("WATSONX_URL"),
    api_key = os.getenv("WATSONX_API_KEY")
)
wx_client = APIClient(credentials)

# the LLM that will generate questions for each chunk
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

answering_model = ModelInference(
            model_id=wx_client.foundation_models.TextModels.MISTRAL_LARGE,
            params={GenParams.DECODING_METHOD: 'greedy',
            GenParams.MIN_NEW_TOKENS: 1,
            GenParams.MAX_NEW_TOKENS: 600,
            GenParams.STOP_SEQUENCES: []
            },
            credentials={
                "apikey": os.getenv("WATSONX_API_KEY"),
                "url": os.getenv("WATSONX_URL"),
            },
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

# %%
# QUESTION ANSWERING
prompt_answer = """Eres el asistente de la base de conocimiento. Contesta a la pregunta indicada abajo, utilizando parcial o totalmente los datos que se te proporcionan como contexto, sin información previa.

    CONTEXTO: '''{}'''

    PREGUNTA: {}

    RESPUESTA: """

def answer_question(question: str, index_name: str, answering_model, embedding_model, prompt: str, streaming: bool = True, search_params=None, context=None, search_results=None):
    """Answers a single question using the knowledge base."""

    if context is None and search_results is None:
        context, search_results = search(question, index_name, embedding_model, search_params)

    if context is None:
        return "No existe contexto para responder a la pregunta.", []

    # # trim context to fit within max length
    # from transformers import AutoTokenizer
    # tokenizer = AutoTokenizer.from_pretrained("fxmarty/tiny-llama-fast-tokenizer")
    # max_context_length = 2500

    # available_tokens = max_context_length - sum(len(tokenizer.encode(text)) 
    #                                                 for text in [question, prompt])
    # context = tokenizer.decode(
    #     tokenizer.encode(context, max_length=available_tokens, truncation=True),
    #     skip_special_tokens=True
    # )

    formatted_prompt = prompt.format(context, question)

    if streaming:
        answer = ""
        for chunk in answering_model.generate_text_stream(formatted_prompt):
            print(chunk, end='')
            answer += chunk
    else:
        answer = answering_model.generate_text(formatted_prompt)

    return answer, search_results

# %%
question = "¿Cómo se hace la renovación automática de la póliza blindaje plus?"
answer, search_results = answer_question(question, index_name, answering_model, embedding_model, prompt_answer, streaming=True)

# %%


# %%
# Alternative approach: Reranking
# It reranks the chunks based on the question
# After reranking, it keeps only the top chunks
# It then uses these chunks to answer the question
from ibm_watsonx_ai.foundation_models import Rerank
from ibm_watsonx_ai.foundation_models.schema import RerankParameters

rerank_params = RerankParameters(truncate_input_tokens = 512)
wx_ranker = Rerank(
    model_id="cross-encoder/ms-marco-minilm-l-12-v2",
    credentials=Credentials(
        api_key = os.getenv("WATSONX_API_KEY"),
        url = os.getenv("WATSONX_URL")
    ),
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

def reranking(query, search_results, rerank_params, top_percentage=0.5):
    # top_percentage = 0.1 means only chunks at the top 10% of the interval [best-worse] will be considered

    response = wx_ranker.generate(query=query, inputs=search_results, params=rerank_params)

    best_score = response['results'][0]['score']
    worst_score = response['results'][-1]['score']
    threshold = best_score - top_percentage * (best_score - worst_score)

    reranked_results = []
    leftout_results = []
    for result in response['results']:
        if result['score'] > threshold:
            reranked_results.append(search_results[result['index']])
        else:
            leftout_results.append(search_results[result['index']])

    reranked_context = "\n\n\n\n".join(hit.text for hit in reranked_results)

    return reranked_context, reranked_results, leftout_results

# %%
# example of reranking
question = "¿Cómo se hace la renovación automática de la póliza blindaje plus?"

search_params = {
        "index": index_name,
        "knn": {
            "field": "embedding",
            "query_vector": embedding_model.embed_documents(texts=['query: ' + question])[0],
            "k": 10,
            "num_candidates": 100
        }
    }

question = "¿Cómo se hace la renovación automática de la póliza blindaje plus?"

context, initial_search_results = search(question, index_name, embedding_model, search_params)
reranked_context, reranked_results, leftout_results = reranking(question, initial_search_results, rerank_params, top_percentage=0.1)
answer, search_results = answer_question(question, index_name, answering_model, embedding_model, prompt_answer, streaming=True, context=reranked_context, search_results=reranked_results)

# %%


# %%
# Alternative approach: Reflection
# It evaluates the relevance of each chunk before answering
# It selects only those chunks that are relevant to the question
from ibm_watsonx_ai import APIClient, Credentials
credentials = Credentials(
    url = os.getenv("WATSONX_URL"),
    api_key = os.getenv("WATSONX_API_KEY")
)
client = APIClient(credentials)

# the LLM that will generate questions for each chunk
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

reflection_model = ModelInference(
            model_id=client.foundation_models.TextModels.MISTRAL_LARGE,
            params={GenParams.DECODING_METHOD: 'greedy',
            GenParams.MIN_NEW_TOKENS: 1,
            GenParams.MAX_NEW_TOKENS: 20,
            GenParams.STOP_SEQUENCES: ['Si', 'Sí', 'sí', 'si', 'No', 'no']
            },
            credentials={
                "apikey": os.getenv("WATSONX_API_KEY"),
                "url": os.getenv("WATSONX_URL"),
            },
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

# %%
def reflection(question: str, search_results: list, reflection_model):
    prompt_reflection = """
            Eres el asistente de la base de conocimiento. Contesta a la pregunta indicada abajo, en base a los datos que se te proporcionan como contexto. Se estricto y basate exclusivamente en la información proporcionada en el documento.

            ¿La informacion dada en el contexto está relacionada con la pregunta? Explicalo, comienza la respuesta con un "Si" o un "No".

            Contexto: '''{}'''

            Pregunta: {}
            
            Respuesta: """

    selected_chunks = []
    leftout_chunks = []

    for hit in search_results:
        relevance, _ = (lambda context: (
        any(term in (answer := reflection_model.generate_text(prompt_reflection.format(context, question))).lower()
            for term in ["sí", "si"]),
        answer))(hit['_source']['text'])
        (selected_chunks if relevance else leftout_chunks).append(hit)

    selected_context = "\n\n\n\n".join(hit['_source']['text'] for hit in selected_chunks)
    
    return selected_context, selected_chunks, leftout_chunks

# %%
# example of reflection
question = "¿Cómo se hace la renovación automática de la póliza blindaje plus?"

search_params = {
        "index": index_name,
        "knn": {
            "field": "embedding",
            "query_vector": embedding_model.embed_documents(texts=['query: ' + question])[0],
            "k": 10,
            "num_candidates": 100
        }
    }

question = "¿Cómo se hace la renovación automática de la póliza blindaje plus?"

context, initial_search_results = search(search_params)
selected_context, selected_search_results, leftout_search_results = reflection(question,
                                                                                initial_search_results, 
                                                                                reflection_model)
answer, search_results = answer_question(question, 
                                         index_name, 
                                         answering_model, 
                                         embedding_model, 
                                         prompt_answer, 
                                         streaming=True, 
                                         context=selected_context, 
                                         search_results=selected_search_results)

# %%



