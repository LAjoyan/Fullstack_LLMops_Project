import os
from pathlib import Path
import mlflow
from pydantic_ai.models.openrouter import OpenRouterModel


ROOT_PATH = Path(__file__).parents[2]
DATA_PATH = ROOT_PATH / "data"

MODEL = OpenRouterModel(
    "openai/gpt-3.5-turbo",
)
EMBEDDING_MODEL = "embed-multilingual-light-v3.0"

# TODO: Verify PROMPTS_PATH works correctly inside Docker containers
PROMPTS_PATH = ROOT_PATH / "prompt_engineering"
MONITORING_PATH = ROOT_PATH / "monitoring"
VECTOR_DB_PATH = ROOT_PATH / "lancedb"
LLM_JUDGE = "openai:/openai/gpt-4o-mini"

mlflow.set_tracking_uri(f"sqlite:///{MONITORING_PATH / 'mlflow.db'}")
TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", f"sqlite:///{MONITORING_PATH / 'mlflow.db'}")
mlflow.set_tracking_uri(TRACKING_URI)

# Setting experiment in MLflow
mlflow.set_experiment("study_buddy_bot")
