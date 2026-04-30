from fastapi import FastAPI
import constants
from data_models import Prompt, RagResponse
from agents import bot_answer
from middleware import logging_middleware

app = FastAPI()

logging_middleware(app=app)

@app.get("/")
async def status():
    return {"status": "it works"}

@app.post("/rag/query")
async def query_documentation(query: Prompt) -> RagResponse:
    result = await bot_answer(query.prompt)
    return resultv