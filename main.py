
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from retrieval import get_response

app = FastAPI()

# Define the request model
class QueryRequest(BaseModel):
    query: str

# API Endpoints
@app.post("/chat")
async def chat(request: QueryRequest):
    try:
        response = get_response(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server: uvicorn main:app --reload
