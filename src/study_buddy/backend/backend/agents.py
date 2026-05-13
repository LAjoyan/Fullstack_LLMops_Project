from pydantic_ai import Agent
import lancedb
from backend.constants import MODEL, VECTOR_DB_PATH
from backend.data_models import RagResponse
from mlflow.genai import load_prompt
import mlflow
import re

vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

try:
    active_system_prompt = load_prompt("prompts:/rag_agent_system_prompt@production")
    print("Successfully loaded system prompt from MLflow.")
except Exception as e:
    print(f"MLflow prompt not found, using fallback prompt. Error: {e}")
    active_system_prompt = """You are a helpful AI teaching assistant.
Use the provided Context to answer the user's question.
If the context doesn't contain the exact answer, you are allowed to use your general AI knowledge to explain the concept to the student.

CRITICAL INSTRUCTION: Keep your answers concise, brief, and directly to the point (maximum 2 to 3 sentences). Do not write long essays or use analogies unless asked.
"""

rag_agent = Agent(
    model=MODEL,
    system_prompt=active_system_prompt,
    retries=3,
)

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
B) [Option B]
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

Task: Create 5 flashcards based on the context.
Focus entirely on the concepts, definitions, and facts.

CRITICAL INSTRUCTIONS:
1. DO NOT mention "this video", "the transcript", "the speaker", or "this lecture". Frame every question as a general, standalone fact (e.g., ask "What is Pydantic AI?" instead of "What is the topic of the video?").
2. You MUST format EVERY flashcard exactly like this on a single line:
Q: [The Question] | A: [The Answer]
3. Do not write "Card 1", do not use bullet points, and do not add an introduction. Just the Q and A separated by the pipe (|) symbol.
"""


@mlflow.trace
async def bot_answer(user_prompt: str):
    try:
        # 1. Manually search the database (No AI tools needed!)
        results = vector_db["LectureTranscript"].search(query=user_prompt).limit(3).to_list()

        if not results:
            context = "No documents found."
            source_doc = "None"
        else:
            # Combine the text from the top documents
            context = "\n\n".join([doc["content"][:1000] for doc in results])
            # Grab the filename of the very best match for the UI
            source_doc = results[0].get('document_name', 'Unknown').replace('.md', '')

        # 2. Build a clear, direct prompt for the AI
        full_prompt = f"""
Context:
{context}

User Question:
{user_prompt}
"""

        # 3. Let the AI generate the answer using the text we just found
        response = await rag_agent.run(full_prompt)

        # 4. Return it nicely to the frontend!
        return RagResponse(
            filename=source_doc,
            filepath="LanceDB Database",
            answer=response.output,
        )

    except Exception as e:
        return RagResponse(
            filename="Error",
            filepath="Error",
            answer=f"An error occurred: {str(e)}",
        )
