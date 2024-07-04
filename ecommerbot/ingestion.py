from ecommerbot.data_converter import dataconveter
import pandas
import os
from dotenv import load_dotenv
from langchain_ai21 import AI21Embeddings
from langchain_qdrant import Qdrant
from together import Together

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
# os.environ["TOGETHER_API_KEY"] = TOGETHER_API_KEY

AI21_API_KEY = os.getenv("mTypqGXPZj2t13dFCiFdd263zZLiBySW")

os.environ["AI21_API_KEY"] = AI21_API_KEY

Qdrant_api = os.getenv("Qdrant")
url_qdrant = os.getenv("url_qdrant")

embeddings = AI21Embeddings()

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
    results = vstore.similarity_search("can you tell me the low budget sound basshead.")
    for res in results:
            print(f"* {res.page_content} [{res.metadata}]")