from pathlib import Path

ROOT_PATH = Path(__file__).parents[2]
DATA_PATH = ROOT_PATH / "data"

VECTOR_DB_PATH =  ROOT_PATH / "lancedb"

MODEL="openrouter:openai/gpt-4.1-nano"
EMBEDDING_MODEL = "embed-multilingual-light-v3.0"