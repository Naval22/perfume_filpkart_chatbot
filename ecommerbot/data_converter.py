import pandas as pd
from langchain_core.documents import  Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def dataconveter():
    product_data = pd.read_csv("D:\\GEN AI\\Perfume_chatbot\\Data\\perfume_data.csv")
    
    data = product_data[["product_name","comment"]]
    
    product_list = []
    
    #Iterate over the rows of the Dataframe
    for index ,row  in data.iterrows():
        
        obj = {
            "product_name" :row["product_name"],
            "comment":row["comment"]
        }
        
        #Append the object into list
        product_list.append(obj)
        
    doces = []
    # docs = []
    for entry in product_list:
        metadata = {"product_name":entry["product_name"]}
        doc = Document(page_content=entry["comment"],metadata= metadata)        
        doces.append(doc)
        # text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=500)
        # docs = text_splitter.split_documents(doces)
        # docs.append(docs)
        # print(docs[0])
    return doces

# if __name__ == "__main__":
#     dataconveter()