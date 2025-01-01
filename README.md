
# Chatbot with Pinecone and GPT-4

This repository contains a fully functional chatbot implementation using Pinecone as a vector database and OpenAI's GPT-4 language model. The chatbot is built using FastAPI for the backend and LangChain for handling embeddings and retrieval.

## Features
- Uses Pinecone for storing and querying vector embeddings.
- OpenAI GPT-4 for natural language responses.
- FastAPI for a simple and scalable REST API.
- Environment variable configuration for secure API key management.

## Prerequisites
- Python 3.9 or later
- Pinecone account with API key
- OpenAI account with API key
- `.env` file for environment variables

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatbot.git
   cd chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with the following variables:
   ```env
   PINECONE_API_KEY=your-pinecone-api-key
   PINECONE_ENV=your-pinecone-environment
   OPENAI_API_KEY=your-openai-api-key
   ```

4. Initialize Pinecone and upload data by running:
   ```bash
   python dataupload.py
   ```

5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## API Usage

### Endpoint: `/chat`
- Method: `POST`
- Request Body:
  ```json
  {
    "query": "Your question here"
  }
  ```
- Response:
  ```json
  {
    "response": "Chatbot's response"
  }
  ```

## Files
- `dataupload.py`: Script for initializing Pinecone and uploading sample data.
- `embedding.py`: Embedding function for vectorization.
- `retrieval.py`: Handles retrieval and LLM response generation.
- `main.py`: FastAPI backend for chatbot communication.

## Contributing
Feel free to fork and submit PRs to improve the functionality or fix issues.

## License
This project is open-source and available.
