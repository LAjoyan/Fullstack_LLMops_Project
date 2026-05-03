import lancedb
from pathlib import Path
from backend.constants import DATA_PATH
from backend.data_models import LectureTranscript

VECTOR_DB_PATH = "./vector_db"

def setup_vector_db(path):
    Path(path).mkdir(exist_ok=True) # skapar mapp om den inte finns
    vector_db = lancedb.connect(uri=path) # kopplar upp mot databasen
    vector_db.create_table("LectureTranscript", schema=LectureTranscript, exist_ok=True)
    return vector_db

def import_files_to_db(table):
    data = []
    for file in DATA_PATH.glob("*.md"): # looping through every file who has .md 
     with open(file) as f:
        content = f.read()
    document_name = file.name
    table.delete(f"docuement_name = '{document_name}'") # delete the old one so its not dubble files

    table.add([{"document_name": file.name, "filepath": str(file), "content": content}]) # Add files to the databas

    if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DB_PATH)
    ingest_docs_to_vector_db(vector_db["LectureTranscript"])