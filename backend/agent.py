from pydantic_ai import Agent
from pydantic_ai.usage import UsageLimits
import lancedb
from backend.constants import MODEL
from mlflow.genai import load_prompt

vector_db = lancedb.connect(uri="./vector_db")

rag_agent = Agent(
    model=MODEL,
    system_prompt=load_prompt("rag_agent_system_prompt").format(max_sentences=3),
)


@rag_agent.tool_plain
def retrieve_documents(query: str, k: int = 3) -> str:
    results = vector_db["articles"].search(query=query).limit(k).to_list()

    if not results:
        return "no documents found."
