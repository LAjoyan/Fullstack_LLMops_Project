import os
from pathlib import Path
import mlflow

ROOT_PATH = Path(__file__).parents[2]
DATA_PATH = ROOT_PATH / "data"

MODEL = "openrouter:openai/gpt-4.1-nano"
EMBEDDING_MODEL = "embed-multilingual-light-v3.0"

# TODO: Verify PROMPTS_PATH works correctly inside Docker containers
PROMPTS_PATH = ROOT_PATH / "prompt_engineering"
MONITORING_PATH = ROOT_PATH / "monitoring"
VECTOR_DB_PATH = ROOT_PATH / "lancedb"
LLM_JUDGE = "openai:/openai/gpt-4o-mini"

# Configure MLflow to use a local SQLite database for experiment tracking
mlflow.set_tracking_uri(f"sqlite:///{MONITORING_PATH / 'mlflow.db'}")
