# %%
# Alternative approach for retrieving documents from the index
# Instead of vectorizing the documents, it uses the LLM to generate questions related to each chunk
# These questions are then vectorized and used to search for the most similar chunks in the index
# It can improve the accuracy of the retrieval, but it's more expensive and slower
# Copy this snippet into your solution. You can find templates in other notebooks of this repo
# You will need to first generate a list of chunks using any of the processors provided in the other notebooks of this repo
# Then the function below will generate a new set of chunks, with each new chunk having a synthetic question related to the original chunk

# %%
# quick example. get some docs in a folder and run this
import os
path = 'docs'
pdf_files = [os.path.join(path, filename) for filename in os.listdir(path) if filename.lower().endswith('.pdf')]

from PDFChunker import PDFChunker
processor = PDFChunker()
chunks = processor.process_files(pdf_files)

# %%
from ibm_watsonx_ai import APIClient, Credentials
import os

credentials = Credentials(
    url = os.getenv("WATSONX_URL"),
    api_key = os.getenv("WATSONX_API")
)
wx_client = APIClient(credentials)

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
        api_key=os.getenv("WATSONX_API"),
        url=os.getenv("WATSONX_URL")
    ),
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

# %%
# the LLM that will generate questions for each chunk
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

contextual_retrieval_model = Model(
            model_id=wx_client.foundation_models.TextModels.MISTRAL_LARGE,
            params={GenParams.DECODING_METHOD: 'greedy',
            GenParams.MIN_NEW_TOKENS: 1,
            GenParams.MAX_NEW_TOKENS: 600,
            GenParams.STOP_SEQUENCES: []
            },
            credentials={
                "apikey": os.getenv("WATSONX_API"),
                "url": os.getenv("WATSONX_URL"),
            },
    project_id=os.getenv("WATSONX_PROJECT_ID")
)

# %%
# contextual retrieval: the function that will generate and embed example questions
import pandas as pd
import json
from typing import List, Dict, Any
from tqdm import tqdm

def generate_and_embed_questions(
    chunks: List[Dict[str, Any]],
    llm_model: Any,
    embedding_model: Any,
    batch_size: int = 1
) -> List[Dict[str, Any]]:
    """
    Generate questions for each text chunk and create embeddings for them.
    
    Args:
        chunks: List of dictionaries containing text chunks and their metadata
        llm_model: Initialized LLM model for question generation
        embedding_model: Initialized embedding model
        batch_size: Number of chunks to process at once for batched operations
    
    Returns:
        List of dictionaries with columns for chunk metadata, generated questions, and their embeddings
    """
    # Template for question generation
    prompt_contextual_questions = """Genera un listado de 10 preguntas cortas para el siguiente fragmento de texto. Retornalas en formato JSON.

Input: [INPUT] Condiciones Generales Súper Blindaje Santander Estimado Cliente, Agradecemos su confianza al haber contratado su Seguro de “Súper Blindaje Santander” con Zurich Santander Seguros México, S.A., para nosotros es un compromiso muy importante garantizar la satisfacción de sus necesidades de protección y prevención, brindando un servicio que cumpla y supere sus expectativas. Para respaldar este compromiso, Zurich Santander Seguros México, S. A., pone a su disposición una infraestructura de servicio a nivel nacional que cuenta con recursos tecnológicos y un equipo de profesionales para atenderle. Le recordamos revisar debidamente la Póliza y sus Condiciones Generales, en estos documentos encontrará los riesgos amparados, sumas aseguradas, el alcance de sus coberturas y qué hacer en caso de siniestro. Si tiene alguna duda o requiere información adicional, nuestros especialistas tendrán el gusto de atenderle y asesorarle en los teléfonos 5169 4300 en la Ciudad de México, o al 01 555169 4300 lada sin costo desde el interior del país. Atentamente, Zurich Santander Seguros México, S. A. [END_INPUT]
Output: ```json
{
  "preguntas": [
    "¿Qué seguro ha contratado el cliente?",
    "¿Qué empresa proporciona el seguro?",
    "¿Qué compromiso tiene la empresa con el cliente?",
    "¿Qué tipo de infraestructura ofrece la empresa?",
    "¿Qué documentos debe revisar el cliente?",
    "¿Qué información encontrará el cliente en la Póliza y sus Condiciones Generales?",
    "¿Qué debe hacer el cliente en caso de siniestro?",
    "¿Qué debe hacer el cliente si tiene dudas o necesita información adicional?",
    "¿Cuál es el número de teléfono para contactar a los especialistas en la Ciudad de México?",
    "¿Cuál es el número de teléfono para contactar a los especialistas desde el interior del país?"
  ]
}
```

Input: [INPUT] {input} [END_INPUT]
Output:"""
    
    # Lists to store all results
    all_records = []
    
    # Process chunks in batches
    for i in tqdm(range(0, len(chunks), batch_size), desc="Processing chunks"):
        batch = chunks[i:i + batch_size]
        
        # Generate questions for each chunk in the batch
        for chunk in batch:
            # Generate questions using the LLM
            generated_text = llm_model.generate_text(
                prompt=prompt_contextual_questions.replace('{input}', chunk['text'])
            )

            # for debugging
            print(generated_text)
            
            # Parse the JSON response
            text_to_parse = generated_text.strip().replace('```json', '').replace('```', '')
            questions_dict = json.loads(text_to_parse)
            
            # Get embeddings for all questions in this chunk
            questions = questions_dict['preguntas']

            question_embeddings = embedding_model.embed_documents(texts=[f"query: {question}" for question in questions])
            
            # Create a record for each question
            for q_idx, (question, embedding) in enumerate(zip(questions, question_embeddings)):

                record = {
                    # Original chunk metadata
                    'document_id': chunk['document_id'],
                    'document_title': chunk['document_title'],
                    'document_page': chunk['document_page'],
                    'chunk_id': chunk['chunk_id'],
                    'text': chunk['text'],
                    'n_tokens': chunk['n_tokens'],
                    
                    # Question data
                    'question_id': f"{chunk['chunk_id']}_{q_idx}",
                    'question': question,
                    'embedding': embedding
                }
                all_records.append(record)
                    
    return all_records

# %%
# generate and embed questions
enhanced_chunks = generate_and_embed_questions(
    chunks=chunks,
    llm_model=contextual_retrieval_model,
    embedding_model=embedding_model
)

# %%
# save the enhanced chunks to a csv file
import pandas as pd
df = pd.DataFrame(enhanced_chunks)
df.to_csv('enhanced_chunks.csv', index=False)

# %%
# in case you want to load the enhanced chunks later on
import pandas as pd
df = pd.read_csv('enhanced_chunks.csv')
enhanced_chunks = df.to_dict(orient='records')

# parse embeddings stored in string format
import ast
for chunk in enhanced_chunks:
    chunk['embedding'] = ast.literal_eval(chunk['embedding'])

# %%
# If using elastic search

# Settings for document processing. note it has more fields than a normal index due to the synthetic questions
index_parameters = {
    'mappings': {
        'properties': {
            'chunk_id': {'type': 'integer'},
            'document_id': {'type': 'integer'},
            'document_title': {'type': 'keyword'},
            'document_page': {'type': 'integer'},
            'n_tokens': {'type': 'integer'},
            'text': {'type': 'text'},
            'question': {'type': 'text'},
            'question_id': {'type': 'keyword'},
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
# If using Milvus
fields = [
            'chunk_id', 'document_id', 'document_title',
            'document_page', 'n_tokens', 'text', 'question',
            'question_id', 'embedding'
        ]

field_schema = [
    FieldSchema(name="chunk_id", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="document_id", dtype=DataType.INT64),
    FieldSchema(name="document_title", dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name="document_page", dtype=DataType.INT64),
    FieldSchema(name="n_tokens", dtype=DataType.INT64),
    FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=65535),
    FieldSchema(name="question", dtype=DataType.VARCHAR, max_length=65535),
    FieldSchema(name="question_id", dtype=DataType.VARCHAR, max_length=255),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1024)
]


