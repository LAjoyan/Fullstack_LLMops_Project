from pydantic import BaseModel, Field
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from constants import EMBEDDING_MODEL
from dotenv import load_dotenv

load_dotenv()

embedding_model = get_registry().get("cohere").create(name=EMBEDDING_MODEL)


class Article(LanceModel):
    document_name: str
    filepath: str
    content: str = embedding_model.SourceField()
    embedding: Vector(embedding_model.ndims()) = embedding_model.VectorField()


class Prompt(BaseModel):
    prompt: str = Field(
        description="prompt from user, if empty consider prompt as missing"
    )


class RagResponse(BaseModel):
    filename: str | None = Field(
        default=None, description="filename of the retrieved file without suffix"
    )
    filepath: str | None = Field(
        default=None, description="absolute path to the retrieved file"
    )
    answer: str | None = Field(
        description="answer based on the retrieved file, concise but captures essential meaning"
    )













