from pydantic_ai import Agent
import lancedb
from backend.constants import MODEL, VECTOR_DB_PATH
from backend.data_models import RagResponse
import re


vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

rag_agent = Agent(
    model=MODEL,
    system_prompt=(
        "You are a helpful, intelligent study assistant. Follow these rules STRICTLY:\n"
        "1. ALWAYS use the `retrieve_documents` tool to gather context before answering.\n"
        "2. Answer the user's question DIRECTLY and naturally. NEVER use phrases like 'The document says...' or 'This file provides...'. Just give the factual answer.\n"
        "3. Answer based ONLY on the retrieved context.\n"
        "4. If the retrieved context does not contain the specific answer to the user's question (e.g., they ask for a date, but no date is in the text), DO NOT summarize the text instead. Reply exactly with: 'I cannot answer this as it is not included in my expertise.'\n"
        "5. Extract the 'Filename' and 'Filepath' from the retrieved context and map them to the structured response. If you cannot answer, set them to 'None'."
    ),
    output_type=RagResponse,
)


@rag_agent.tool_plain
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


@rag_agent.tool_plain
def generate_quiz(user_query: str, k: int = 1) -> str:  # reducing nnumber of docs

    # 1. Extract number of questions (default = 5)
    match = re.search(r"\d+", user_query)
    num_questions = int(match.group()) if match else 5
    num_questions = min(num_questions, 2)
    # 2. Extract topic
    topic = user_query.lower().replace("quiz", "").strip()
    if not topic:
        topic = "machine learning"  # fallback

    # 3. Retrieve from LanceDB (semantic search works because of embeddings)
    results = vector_db["LectureTranscript"].search(topic).limit(k).to_list()

    if not results:
        return "No relevant content found."

    # 4. Combine context
    context = "\n\n".join(
        [doc["content"][:150] for doc in results]
    )  # reducing context size

    return f"""
Topic: {topic}

Context:
{context}

Task:
Generate {num_questions} multiple choice questions.

Requirements:
- 4 options (A-D) , keep every option in a separate line
- Keep questions short
- The user must provide and you say if it's correct or wrong
- If it's wrong you explain why the selected answer was wrong
"""


@rag_agent.tool_plain
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


async def bot_answer(user_prompt: str):
    try:
        user_lower = user_prompt.lower()

        # 🚀 Bypass agent for quiz
        if "quiz" in user_lower:
            prompt = generate_quiz(user_prompt)
            response = await rag_agent.run(prompt)
            answer = response.output.answer

            return RagResponse(
                filename="Quiz",
                filepath="Generated",
                answer=answer,
            )

        # 🚀 Bypass agent for flashcards
        if "flashcards" in user_lower:
            prompt = generate_flashcards(user_prompt)
            response = await rag_agent.run(prompt)
            answer = response.output.answer

            return RagResponse(
                filename="Flashcards",
                filepath="Generated",
                answer=answer,
            )

        # ✅ Only use agent for normal Q&A
        response = await rag_agent.run(user_prompt)
        return response.output

    except Exception as e:
        return RagResponse(
            filename="Error",
            filepath="Error",
            answer=f"An error occurred: {str(e)}",
        )
