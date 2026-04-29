from pydantic_ai import Agent
from pydantic_ai.usage import UsageLimits
import lancedb
from backend.constants import MODEL

vector_db = lancedb.connect(uri="./vector_db")

best_agent = Agent(
    model = MODEL,
    system_prompt = "You are a expert reader and doing quizes and summarize youtube subtitle files"
)