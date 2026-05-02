
from dotenv import load_dotenv
load_dotenv() 
from pydantic_ai import Agent
import lancedb
from backend.constants import MODEL, VECTOR_DB_PATH
from backend.data_models import RagResponse

vector_db = lancedb.connect(uri=VECTOR_DB_PATH)

rag_agent = Agent(
    model=MODEL,
    system_prompt="You are an expert reader. Answer questions and summarize based on the retrieved documents.",
    output_type=RagResponse, 
)

@rag_agent.tool_plain 
def retrieve_documents(query: str, k: int=3) -> str:
    results = vector_db["LectureTranscript"].search(query=query).limit(k).to_list()

    if not results:
        return "No documents found."
        
   
    return "\n\n".join(
        f"Filename: {doc.get('document_name', 'Unknown').replace('.md', '')}\n"
        f"Filepath: {doc.get('filepath', 'Unknown')}\n"
        f"Content: {doc['content']}"
        for doc in results
    )


async def bot_answer(user_prompt: str):
    try:
        response = await rag_agent.run(user_prompt)
        return response.output
    except Exception as e:
        return RagResponse(
            filename="Error",
            filepath="Error",
            answer=f"Något gick fel i Agenten: {str(e)}"
        )