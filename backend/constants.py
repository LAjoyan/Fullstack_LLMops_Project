from pathlib import Path

ROOT_PATH = Path(__file__).parents[1]
DATA_PATH = ROOT_PATH / "data"

VECTOR_DB_PATH = ROOT_PATH / "knowledge_base"

MODEL="openrouter:openai/gpt-4.1-nano"
EMBEDDING_MODEL = "embed-multilingual-light-v3.0"