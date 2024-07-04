import pandas as pd
from langchain_core.documents import  Document


def dataconveter():
    product_data = pd.read_csv("../Data/perfume_data.csv")
    
    data = product_data[["product_name","description","comment"]]
    
    product_list = []
    
    #Iterate over the rows of the Dataframe
    for index ,row  in data.iterrows():
        
        obj = {
            "product_name" :row["product_name"],
            "description" :row["description"],
            "comment":row["comment"]
        }
        
        #Append the object into list
        product_list.append(obj)
        
    docs = []
    for entry in product_list:
        metadata = {"product_name":entry["product_name"]}
        doc = Document(page_content=entry["description","comment"],metadata= metadata)        
        docs.append(doc)
    return docs

