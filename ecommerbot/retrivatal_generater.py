from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_together import ChatTogether
from ecommerbot.ingestion import ingestdata

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k":3})
    
    PERFUME_BOT_TEMPLATE = """
    Your perfumebot is an expert in perfume recommendations and customer queries.
    It analyzes perfume names, descriptions, and customer comments to provide accurate and helpful responses.
    Ensure your answers are relevant to the perfume context and refrain from straying off-topic.
    Your responses should be concise and informative.OUTPUT LIKE : PRODUCT NAME ,DESCRICPTION AND COMMENT OF USER THIS FORMATE FOLLOW FOR OUTPUT.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:

    """
    
    prompt = ChatPromptTemplate.from_template(PERFUME_BOT_TEMPLATE)
    
    llm = ChatTogether(model="meta-llama/Llama-3-70b-chat-hf",temperature= 0,streaming =True)
    
    chain = (
        {"context":retriever,"question":RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if  __name__ == "__main__":
    vstore = ingestdata()
    chain = generation(vstore)
    print(chain.invoke("can you suggest me best perfume?"))