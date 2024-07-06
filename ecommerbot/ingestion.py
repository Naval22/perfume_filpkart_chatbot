from langchain_astradb import AstraDBVectorStore
from langchain_ai21 import AI21Embeddings
from langchain_qdrant import Qdrant
from together import Together
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from dotenv import load_dotenv
import os
import pandas as pd
from ecommerbot.data_converter import dataconveter

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
AI21_API_KEY = os.getenv("AI21_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

# embedding = AI21Embeddings()
model_name = "jinaai/jina-embeddings-v2-base-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embedding = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

def ingestdata():
    data = dataconveter()
    
    # if isinstance(data, list):
    #     if all(isinstance(item, Document) for item in data):
    #         documents = data
    #     elif all(isinstance(item, list) for item in data):
    #         documents = [Document(page_content=item[0], metadata={"source": item[1] if len(item) > 1 else None}) for item in data]
    #     else:
    #         raise ValueError("Unexpected data format from dataconveter()")
    # else:
    #     raise ValueError("dataconveter() should return a list")
    
    vstore = AstraDBVectorStore.from_documents(
        data,
        embedding=embedding,
        collection_name="chatbotecos",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )
    # storage=status
    
    return vstore
    
# if __name__=='__main__':
#     vstore=ingestdata()
#     # print(f"\nInserted {len(inserted_ids)} documents.")
#     results = vstore.similarity_search("can you tell me the low budget perfume.")
#     print(results[0])
    # for res in results:
    #         print(f"* {res.page_content} [{res.metadata}]")
            

