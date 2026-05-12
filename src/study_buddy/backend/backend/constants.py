import os
from pathlib import Path
import mlflow


ROOT_PATH = Path(__file__).parents[2]
DATA_PATH = ROOT_PATH / "data"

MODEL = "openrouter:meta-llama/llama-3.1-8b-instruct"

EMBEDDING_MODEL = "embed-multilingual-light-v3.0"

# TODO: Verify PROMPTS_PATH works correctly inside Docker containers
PROMPTS_PATH = ROOT_PATH / "prompt_engineering"
MONITORING_PATH = ROOT_PATH / "monitoring"
VECTOR_DB_PATH = ROOT_PATH / "lancedb"
LLM_JUDGE = "openai/gpt-4o-mini"

mlflow.set_tracking_uri(f"sqlite:///{MONITORING_PATH / 'mlflow.db'}")
TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", f"sqlite:///{MONITORING_PATH / 'mlflow.db'}")
mlflow.set_tracking_uri(TRACKING_URI)

# Setting experiment in MLflow
mlflow.set_experiment("study_buddy_bot")
