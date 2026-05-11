import os
import mlflow
from backend.constants import LLM_JUDGE, MONITORING_PATH

db_path = MONITORING_PATH / "mlflow.db"
if db_path.exists():
    os.chmod(db_path, 0o666)

mlflow.set_experiment("rag_evaluation")

import lancedb
import asyncio
import nest_asyncio
from backend.constants import VECTOR_DB_PATH
from backend.agents import bot_answer

nest_asyncio.apply()

vector_db = lancedb.connect(uri=VECTOR_DB_PATH)
docs = vector_db["LectureTranscript"].to_pandas()

evaluation_dataset = [
    {
        "inputs": {
            "prompt": row["document_name"],
            "context": row["content"],
        },
    }
    for _, row in docs.head(2).iterrows()
]

def predict_fn(prompt, context=None):
    result = asyncio.get_event_loop().run_until_complete(bot_answer(prompt))
    return result.answer

import requests
import json
from mlflow.genai import evaluate
from mlflow.genai.scorers import scorer

RELEVANCE_PROMPT = """Rate from 1-5 how well the answer addresses the question.
Question: {inputs}
Answer: {outputs}
Respond ONLY with JSON: {{"score": <1-5>}}"""

GROUNDEDNESS_PROMPT = """You are evaluating if an answer is grounded in the provided context.

STRICT RULES:
- Use ONLY the context below. Do NOT use any outside knowledge.
- Score 5: every claim in the answer is directly supported by the context
- Score 3: most claims are supported, but some are not in the context
- Score 1: the answer contains claims that are NOT in the context (hallucinations)

Question: {inputs}
Answer: {outputs}

Context (the only source of truth):
{context}

Respond ONLY with JSON: {{"score": <1-5>, "reason": "<brief explanation>"}}"""


def judge(prompt: str) -> int:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"},
        json={
            "model": "openai/gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
        },
    )
    text = response.json()["choices"][0]["message"]["content"]
    try:
        return int(json.loads(text)["score"])
    except Exception:
        return 0


@scorer
def relevance(inputs, outputs):
    return judge(RELEVANCE_PROMPT.format(inputs=inputs, outputs=outputs))


@scorer
def groundedness(inputs, outputs):
    return judge(GROUNDEDNESS_PROMPT.format(
        inputs=inputs["prompt"],
        outputs=outputs,
        context=inputs["context"]
    ))


scorers = [relevance, groundedness]

with mlflow.start_run(run_name="rag_evaluation"):
    results = evaluate(data=evaluation_dataset, predict_fn=predict_fn, scorers=scorers)

results
