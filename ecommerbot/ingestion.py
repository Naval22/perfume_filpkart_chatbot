from ecommerbot.data_converter import data
import pandas
import os
import getpass
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_qdrant import Qdrant
from together import Together

# os.environ["GOOGLE_API_KEY"] = getpass("")

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
# os.environ["TOGETHER_API_KEY"] = TOGETHER_API_KEY

Huggingface_API = os.getenv("Huggingface_API")

# os.environ["AI21_API_KEY"] = AI21_API_KEY

Qdrant_api = os.getenv("Qdrant")
url_qdrant = os.getenv("url_qdrant")


embeddings = HuggingFaceEmbeddings(
    model_name="jinaai/jina-embeddings-v2-base-en",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': False},
    api_key = Huggingface_API,
)

def ingestdata(status):
    vstore = Qdrant.from_documents(
        documents = docs,
        embeddings=embeddings,
        url = url_qdrant,
        collection_name = "cluster0",
        api_key = Qdrant_api
    )
    
    storage = status
    
    if storage == None :
        docs = dataconveter()
        inserted_ids = vstore.add_documents(docs)
    else :
        return vstore
    return vstore ,inserted_ids

if __name__ == "__main__":
    vstore, inserted_ids = ingestdata(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell me the best denver perfume.")
    for res in results:
            print(f"* {res.page_content} [{res.metadata}]")