
from langchain.embeddings import OpenAIEmbeddings
import os

# Embedding function using OpenAI
def get_embeddings():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=openai_api_key)
