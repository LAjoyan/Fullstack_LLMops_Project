import re
import lancedb
from pydantic_ai import Agent
from .data_models import RagResponse
from .constants import MODEL, VECTOR_DB_PATH

# Connect to database
vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

# Initialize Agent
rag_agent = Agent(
    model=MODEL,
    system_prompt=(
        "You are a helpful, intelligent study assistant. "
        "Use the retrieve_documents tool to get information from lecture notes. "
        "RULES:\n"
        "1. For REGULAR QUESTIONS: Answer naturally. At the end, add: SOURCE_FILE: [filename].\n"
        "2. For QUIZZES: Generate EXACTLY 5 multiple-choice questions. "
        "YOU MUST FORMAT EVERY QUESTION EXACTLY LIKE THIS:\n\n"
        "Question X: [The question text]\n"
        "- A)[Option A]\n"
        "- B) [Option B]\n"
        "- C) [Option C]\n"
        "- D) [Option D]\n\n"
        "You MUST use the hyphen (-) before A, B, C, and D to force a bulleted list! "
        "After all 5 questions, type '---FACIT---' on a new line. "
        "After '---FACIT---', you MUST provide the correct answers for ALL 5 questions in a numbered list (1 to 5).\n"
        "3. For FLASHCARDS: Format as 'Q: [Question] | A: [Answer]'. One card per line."
    )
)

@rag_agent.tool_plain
def retrieve_documents(query: str, k: int = 3) -> str:
    try:
        table = vector_db["LectureTranscript"]
        results = table.search(query=query).limit(k).to_list()
        if not results:
            return "No documents found."
        return "\n\n".join([f"FILE: {doc.get('document_name')}\nCONTENT: {doc['content']}" for doc in results])
    except Exception as e:
        return f"Error: {str(e)}"

def generate_quiz(user_query: str) -> str:
    topic = user_query.lower().replace("quiz", "").strip() or "the material"
    return (
        f"Create a 5-question quiz about {topic}. "
        "Remember the STRICT FORMAT: Use a hyphen (-) before options A, B, C, and D. "
        "Provide all 5 questions, then '---FACIT---', then ALL 5 answers."
    )

def generate_flashcards(user_query: str) -> str:
    topic = user_query.lower().replace("flashcards", "").strip() or "the material"
    return f"Create 5 flashcards for {topic} using 'Q: | A:' format."

async def bot_answer(user_prompt: str) -> RagResponse:
    try:
        result = await rag_agent.run(user_prompt)
        full_text = result.data if hasattr(result, 'data') else str(result)
        if hasattr(result, 'output'): full_text = str(result.output)

        # Source extraction
        source_name = "Knowledge Base"
        clean_answer = full_text
        if "SOURCE_FILE:" in full_text:
            parts = full_text.split("SOURCE_FILE:")
            clean_answer = parts[0].strip()
            source_name = parts[1].strip()

        return RagResponse(answer=clean_answer, filename=source_name, filepath="Internal")
    except Exception as e:
        return RagResponse(answer=f"Error: {str(e)}", filename="Error", filepath="Error")
