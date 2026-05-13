from dotenv import load_dotenv  # this must be at the top otherwise won't work

load_dotenv()
from fastapi import FastAPI
from backend.data_models import Prompt, RagResponse
from backend.agents import bot_answer, generate_quiz, generate_flashcards, rag_agent
from backend.middlewares import logging_middleware

app = FastAPI()
# logging_middleware(app=app) # TODO: Activate when ready


@app.get("/")
async def status():
    return {"status": "it works"}


@app.post("/rag/query")
async def query_documentation(query: Prompt) -> RagResponse:
    result = await bot_answer(query.prompt)
    return result


@app.post("/rag/quiz")
async def create_quiz(query: Prompt) -> RagResponse:
    prompt = generate_quiz(query.prompt)
    response = await rag_agent.run(prompt)
    return RagResponse(
        filename="Quiz", filepath="Generated", answer=response.output
    )


@app.post("/rag/flashcards")
async def create_flashcards(query: Prompt) -> RagResponse:
    prompt = generate_flashcards(query.prompt)
    response = await rag_agent.run(prompt)
    return RagResponse(
        filename="Flashcards", filepath="Generated", answer=response.output
    )
