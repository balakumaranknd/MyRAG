from dotenv import load_dotenv
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def setup_rag_system():
    
    loader = TextLoader('my_document.txt', encoding='utf-8')
    documents = loader.load()

    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    
    document_chunks = splitter.split_documents(documents)
     # Initialize embeddings with OpenAI API key
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

    
    # Create FAISS vector store from document chunks and embeddings
    vector_store = FAISS.from_documents(document_chunks, embeddings)

   # Return the retriever for document retrieval with specified search_type
    retriever = vector_store.as_retriever(
       search_type="similarity",  # or "mmr" or "similarity_score_threshold"
       search_kwargs={"k": 5}  # Adjust the number of results if needed
   )
    return retriever

def get_rag_response(query: str):
    
    retriever = setup_rag_system()

    prompt = ChatPromptTemplate.from_template("""
        Answer the question based only on the context.

        Context:
        {context}

        Question:
        {question}
        """)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=openai_api_key,
        temperature=0
    )

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)

    response = rag_chain.invoke(query)
        
  
    return  response

    