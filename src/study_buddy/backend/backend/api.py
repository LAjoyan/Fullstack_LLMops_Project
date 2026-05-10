from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from .data_models import Prompt, RagResponse
from .agent import bot_answer, generate_quiz, generate_flashcards, rag_agent

app = FastAPI()

@app.get("/")
async def status():
    return {"status": "it works"}

@app.post("/rag/query")
async def query_documentation(query: Prompt) -> RagResponse:
    user_input = query.prompt.lower()
    
    if "quiz" in user_input or "flashcards" in user_input:
        if "quiz" in user_input:
            prompt_text = generate_quiz(query.prompt)
        else:
            prompt_text = generate_flashcards(query.prompt)
            
        result = await rag_agent.run(prompt_text)
        
        # FIX: Hämta endast texten (output), inte hela objektet
        # Baserat på din bild heter attributet 'output'
        answer_text = result.output if hasattr(result, 'output') else str(result)
        
        return RagResponse(
            answer=answer_text, 
            filename="Study Material Generator", 
            filepath="Internal"
        )
    
    return await bot_answer(query.prompt)
