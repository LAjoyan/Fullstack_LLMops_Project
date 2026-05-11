from pydantic_ai import Agent
import lancedb
from backend.constants import MODEL, VECTOR_DB_PATH
from backend.data_models import RagResponse
from mlflow.genai import load_prompt
import mlflow
import re

vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

rag_agent = Agent(
    model=MODEL,
    system_prompt=load_prompt("rag_agent_system_prompt"),
    output_type=RagResponse,
)


@rag_agent.tool_plain
@mlflow.trace
def retrieve_documents(query: str, k: int = 3) -> str:
    results = vector_db["LectureTranscript"].search(query=query).limit(k).to_list()

    if not results:
        return "No documents found."

    return "\n\n".join(
        f"DOCUMENT:\n"
        f"Filename: {doc.get('document_name', 'Unknown').replace('.md', '')}\n"
        f"Filepath: {doc.get('filepath') or 'Not found'}\n"
        f"Content: {doc['content'][:1000]}"
        for doc in results
    )


@mlflow.trace
def generate_quiz(user_query: str, k: int = 3) -> str:

    # 1. Extract number of questions (default = 5)
    match = re.search(r"\d+", user_query)
    num_questions = int(match.group()) if match else 5
    num_questions = min(num_questions, 5)
    # 2. Extract topic
    topic = user_query.lower().replace("quiz", "").strip()
    if not topic:
        topic = "machine learning"  # fallback

    # 3. Retrieve from LanceDB (semantic search works because of embeddings)
    results = vector_db["LectureTranscript"].search(topic).limit(k).to_list()

    if not results:
        return "No relevant content found."

    # 4. Combine context
    context = "\n\n".join([doc["content"][:300] for doc in results])

    return f"""
Topic: {topic}

Context:
{context}

Task:
Generate 1 multiple choice question based on the context.

You MUST format your response EXACTLY like this:
QUESTION: [The question]
A) [Option A]
B)[Option B]
C) [Option C]
D) [Option D]
---
CORRECT_ANSWER: [Just the letter A, B, C, or D]
EXPLANATION:[Brief explanation of why the answer is correct and others are wrong]
"""


@mlflow.trace
def generate_flashcards(user_query: str, k: int = 1) -> str:

    topic = user_query.lower().replace("flashcards", "").strip()
    if not topic:
        topic = "machine learning"

    results = vector_db["LectureTranscript"].search(query=topic).limit(k).to_list()

    if not results:
        return "No relevant content found."

    context = "\n\n".join([doc["content"][:150] for doc in results])

    return f"""
Topic: {topic}

Context:
{context}

Task: Create flashcards (Q/A format).
"""


@mlflow.trace
async def bot_answer(user_prompt: str):
    try:
        response = await rag_agent.run(user_prompt)
        return response.output

    except Exception as e:
        return RagResponse(
            filename="Error",
            filepath="Error",
            answer=f"An error occurred: {str(e)}",
        )
