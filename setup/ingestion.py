import lancedb
from pathlib import Path
from backend.constants import DATA_PATH
# from rag.backend.data_models import Article, aktivera sen

def setup_vector_db(path):
    Path(path).mkdir(exist_ok=True) # skapar mapp om den inte finns
    vector_db = lancedb.connect(uri=path) # kopplar upp mot databasen
    vector_db.create_table() # lägg till seanre
    return vector_db

def import_files_to_db(table):
    for file in DATA_PATH ("*.md"):
     with open(file) as f:
        content = f.read()
