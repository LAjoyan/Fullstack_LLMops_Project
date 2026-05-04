from pathlib import Path
import mlflow
import os

ROOT_PATH = Path(__file__).parents[1]
DATA_PATH = ROOT_PATH / "data"

# TODO: Verify PROMPTS_PATH works correctly inside Docker containers
PROMPTS_PATH = ROOT_PATH / "prompt_engineering"

VECTOR_DB_PATH = ROOT_PATH / "knowledge_base"

MODEL = "openrouter:openai/gpt-4.1-nano"
EMBEDDING_MODEL = "embed-multilingual-light-v3.0"

MLFLOW_DB = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5001/")

mlflow.set_track