from pydantic_ai import Agent
from pydantic_ai.usage import UsageLimits
import lancedb
from backend.constants import MODEL
import re

vector_db = lancedb.connect(uri="./vector_db")

rag_agent = Agent(
    model=MODEL,
    system_prompt="""
You are a helpful learning assistant.

You can:
- retrieve documents
- generate quizzes
- create flashcards

Use the appropriate tool based on the user request.
""",
)


@rag_agent.tool_plain
def retrieve_documents(query: str, k: int = 3) -> str:
    results = vector_db["LectureTranscript"].search(query=query).limit(k).to_list()

    if not results:
        return "No documents found."
    return "\n\n".join([doc["content"] for doc in results])


@rag_agent.tool_plain
def generate_quiz(user_query: str, k: int = 3) -> str:

    # 1. Extract number of questions (default = 5)
    match = re.search(r"\d+", user_query)
    num_questions = int(match.group()) if match else 5

    # 2. Extract topic
    topic = user_query.lower().replace("quiz", "").strip()
    if not topic:
        topic = "machine learning"  # fallback

    # 3. Retrieve from LanceDB (semantic search works because of embeddings)
    results = vector_db["LectureTranscript"].search(topic).limit(k).to_list()

    if not results:
        return "No relevant content found."

    # 4. Combine context
    context = "\n\n".join([doc["content"] for doc in results])

    # 5. Prompt
    prompt = f"""
    You are a helpful teacher.

    Create {num_questions} multiple choice quiz questions based ONLY on the content below.

    Content:
    {context}

    Requirements:
    - 4 options per question (A, B, C, D)
    - Clearly mark the correct answer
    - Make questions clear and not too long
    - Avoid repeating the same idea
    """

    return rag_agent.model(prompt)


@rag_agent.tool_plain
def generate_flashcards(user_query: str, k: int = 3) -> str:

    topic = user_query.lower().replace("flashcards", "").strip()
    if not topic:
        topic = "machine learning"

    results = vector_db["LectureTranscript"].search(query=topic).limit(k).to_list()

    if not results:
        return "No relevant content found."

    context = "\n\n".join([doc["content"] for doc in results])

    prompt = f"""
Create study flashcards based ONLY on this content:

{context}

Format:
Q: question
A: short clear answer

Rules:
- Keep answers concise
- Focus on key concepts
- Avoid duplicates
"""

    return rag_agent.model(prompt)
