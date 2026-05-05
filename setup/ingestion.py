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

from backend.constants import DATA_PATH, VECTOR_DB_PATH

from backend.data_models import LectureTranscript


def setup_vector_db(path):

    Path(path).mkdir(parents=True, exist_ok=True)
    
    vector_db = lancedb.connect(uri=path)
    
    table = vector_db.create_table("LectureTranscript", schema=LectureTranscript, exist_ok=True)
    return vector_db, table

def import_files_to_db(table):
    # Letar upp alla Markdown-filer
    md_files = list(DATA_PATH.glob("*.md"))
    
    if not md_files:
        print("Found no .md files in the data folder!")
        return

    for file in md_files:
        # Opens the file and forces UTF‑8 for å, ä, ö
        with open(file, encoding="utf-8") as f:
            content = f.read()

        document_name = file.name
        
        table.delete(f"document_name = '{document_name}'") 

        table.add([{
            "document_name": document_name, 
            "filepath": str(file), 
            "content": content
        }]) 
        print(f"Added ‘{document_name}’ to the database!")

    print("Files in the database right now:")
    print(table.to_pandas()["document_name"]) 

    if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DB_PATH)
    ingest_docs_to_vector_db(vector_db["LectureTranscript"])

if __name__ == "__main__":      
    vector_db, table = setup_vector_db(VECTOR_DB_PATH)
    import_files_to_db(table)