import lancedb
from pathlib import Path

def setup_vector_db(path):
    Path(path).mkdir(exist_ok=True)