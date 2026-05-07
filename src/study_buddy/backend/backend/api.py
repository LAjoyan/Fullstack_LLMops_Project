from dotenv import load_dotenv  # this must be at the top otherwise won't work

load_dotenv()
from fastapi import FastAPI
from backend.data_models import Prompt, RagResponse
from backend.agents import bot_answer

app = FastAPI()


@app.get("/")
async def status():
    return {"status": "it works"}


@app.post("/rag/query")
async def query_documentation(query: Prompt) -> RagResponse:
    result = await bot_answer(query.prompt)
    return result
