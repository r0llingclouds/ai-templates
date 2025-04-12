import sys
import os
import dotenv
import json

project_root = os.path.abspath(os.path.join(os.getcwd(), '../..'))
if project_root not in sys.path:
    sys.path.append(project_root)

dotenv.load_dotenv()

# Initialize the config objects (these will load from .env)
from cv_agent.env import MilvusConfig, EmbeddingsConfig
milvus_config = MilvusConfig()
embeddings_config = EmbeddingsConfig()

# Create MilvusClient instance
from cv_agent.connectors.MilvusClient import MilvusClient
milvus_client = MilvusClient(config=milvus_config, embeddingsconfig=embeddings_config)

collection_name = os.getenv("MILVUS_COLLECTION", "job_recommendations")

if milvus_client.client.has_collection(collection_name):
    print(f"Collection {collection_name} already exists. Skipping.")
else:
    print(f"Collection {collection_name} does not exist. Creating...")
    job_positions_file_path = "job_positions.json"
    with open(job_positions_file_path, 'r') as f:
        job_positions = json.load(f)
    result = milvus_client.create_and_load_collection(collection_name, job_positions)
