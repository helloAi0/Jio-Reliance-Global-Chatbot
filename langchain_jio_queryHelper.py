import os
from dotenv import load_dotenv

# Modern Gemini & Vector Store Imports
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.csv_loader import CSVLoader

# The modern, stable way to import Prompts and Chains
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA

# Load environment variables from .env file
load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)

# Load Reliance Data from CSV
loader = CSVLoader(file_path='jio_customer_support_dataset.csv', source_column='prompt')
data = loader.load()

# Create Embeddings using Google's native model
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# Create and Save Vector Database using FAISS
vector_db_path = "faiss_index_reliance"

# Check if index exists to avoid re-creating every time
if not os.path.exists(vector_db_path):
    print("Creating new Vector Database with Gemini Embeddings...")
    vectordb = FAISS.from_documents(documents=data, embedding=embeddings)
    vectordb.save_local(vector_db_path)
else:
    print("Loading existing database...")
    vectordb = FAISS.load_local(
        vector_db_path, 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    
#Setup Retrieval QA Chain
prompt_template = """Given the following context and a question, generate an answer based on this context only.
If the answer is not in the context, say "I am sorry, I don't have information on that for Reliance."

CONTEXT: {context}
QUESTION: {question}"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(),
    input_key="query",
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

def get_jio_response(user_query):
    """Function called by main.py to get the answer"""
    response = chain.invoke({"query": user_query})
    # We return a dictionary so main.py can access ['result']
    return {"answer": response["result"]}