import lancedb
from pathlib import Path
from dotenv import load_dotenv

load_dotenv() 

from backend.constants import DATA_PATH, VECTOR_DB_PATH

from backend.data_models import LectureTranscript

VECTOR_DB_PATH = DATA_PATH / "lancedb"

def setup_vector_db(path):

    Path(path).mkdir(parents=True, exist_ok=True)
    
    vector_db = lancedb.connect(uri=path)
    
    table = vector_db.create_table("LectureTranscript", schema=LectureTranscript, exist_ok=True)
    return vector_db, table

def import_files_to_db(table):
    # Letar upp alla Markdown-filer
    md_files = list(DATA_PATH.glob("*.md"))
    
    if not md_files:
        print("Hittade inga .md-filer i data-mappen!")
        return

    for file in md_files:
        # Öppnar filen och tvingar utf-8 för å, ä, ö
        with open(file, encoding="utf-8") as f:
            content = f.read()

        document_name = file.name
        
        table.delete(f"document_name = '{document_name}'") 

        table.add([{
            "document_name": document_name, 
            "filepath": str(file), 
            "content": content
        }]) 
        print(f"✅ Lade till '{document_name}' i databasen!")

    print("\nFiler i databasen just nu:")
    print(table.to_pandas()["document_name"]) 

if __name__ == "__main__":      
    vector_db, table = setup_vector_db(VECTOR_DB_PATH)
    import_files_to_db(table)

