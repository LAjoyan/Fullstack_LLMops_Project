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
    for file in DATA_PATH.glob("*.md"): # looping through every file who has .md 
     with open(file) as f:
        content = f.read()

    document_name = file.name
    table.delete(f"docuement_name = '{document_name}'") # delete the old one so its not dubble files

    table.add([{"document_name": file.name, "filepath": str(file), "content": content}]) # Add files to the databas

    print(table.to_pandas()["document_name"]) # Making table to pandas table

