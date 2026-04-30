from pydantic_ai import Agent
from pydantic_ai.usage import UsageLimits
import lancedb
from backend.constants import MODEL
from dotenv import load_dotenv
import asyncio

load_dotenv()

vector_db = lancedb.connect(uri="./vector_db")

rag_agent = Agent(
    model = MODEL,
    system_prompt = "You are a expert reader and doing quizes and summarize youtube subtitle files"
)

@rag_agent.tool_plain 
def retrieve_documents(query: str, k: int=3) -> str:
    results = vector_db["LectureTranscript"].search(query=query).limit(k).to_list()

    if not results:
        return "no documents found."
    return "\n\n".join([r["content"] for r in results])  

async def main():
    result = await rag_agent.run("Summarize the documents")
    print(result.output)

asyncio.run(main())

print(vector_db.table_names())

# Adding mlflow later