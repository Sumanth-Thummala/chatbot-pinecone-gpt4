
import pinecone
import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# Create/Open Index
index_name = "chatbot"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536, metric="cosine")
index = pinecone.Index(index_name)

# Embedding Model
embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Example Data
documents = [
    {"id": "doc1", "text": "What is your return policy?"},
    {"id": "doc2", "text": "How do I reset my password?"},
    {"id": "doc3", "text": "What are your customer support hours?"}
]

# Upload Data
vectors = []
for doc in documents:
    embedding = embedding_model.embed_query(doc["text"])
    vectors.append({"id": doc["id"], "values": embedding, "metadata": {"text": doc["text"]}})

index.upsert(vectors=vectors)

print("Data uploaded successfully!")
