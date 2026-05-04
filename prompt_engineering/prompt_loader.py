# TODO: Store these prompt files in a Docker volume
from backend.constants import PROMPTS_PATH
from mlflow.genai import register_prompt

def register_system_prompts(**kwargs):
    """Registers all .md prompt templates in PROMPTS_PATH in MLflow."""
    for filepath in PROMPTS_PATH.rglob("*.md"):
        with open(filepath, encoding="utf-8") as file:
            filename = filepath.stem
            prompt = file.read()
        
        register_prompt(name=filename, template=prompt, **kwargs)

if __name__ == "__main__":
    register_system_prompts() 