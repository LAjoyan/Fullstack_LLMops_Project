from fastapi import FastAPI
from backend.data_models import Prompt, RagResponse
from backend.agent import bot_answer


app = FastAPI()

@app.get("/")
async def status():
    return {"status": "it works"}

@app.post("/rag/query")
async def query_documentation(query: Prompt) -> RagResponse:
    result = await bot_answer(query.prompt)
    return result