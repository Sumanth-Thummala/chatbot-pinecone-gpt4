
import pinecone
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import Pinecone as PineconeStore
from embedding import get_embeddings
import os

# Initialize Pinecone
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

index_name = "chatbot"

# Load VectorStore
index = pinecone.Index(index_name)
vector_store = PineconeStore(index, embedding_function=get_embeddings())

# Initialize LangChain
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(model="gpt-4", openai_api_key=openai_api_key)
retrieval_qa = RetrievalQA(llm=llm, retriever=vector_store.as_retriever())

def get_response(query):
    return retrieval_qa.run(query)
