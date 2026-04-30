from fastapi import FastAPI
from data_models import Prompt, RagResponse

app = FastAPI()


@app.get("/")
async def status():
    return {"status": "it works"}

@app.post("/rag/query")
async def query_documentation(query: Prompt) -> RagResponse:
  
    return RagResponse(answer="This is a placeholder answer until agent.py is created.")
