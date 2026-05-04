from pydantic import BaseModel, Field
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from backend.constants import EMBEDDING_MODEL
from dotenv import load_dotenv

load_dotenv()

embedding_model = get_registry().get("cohere").create(name=EMBEDDING_MODEL)


class LectureTranscript(LanceModel):
    document_name: str
    filepath: str
    content: str = embedding_model.SourceField()
    embedding: Vector(embedding_model.ndims()) = embedding_model.VectorField()


class Prompt(BaseModel):
    prompt: str = Field(
        description="The input question from the user. Treat empty strings as missing input."
    )


class RagResponse(BaseModel):
    filename: str | None = Field(
        default=None, description="Name of the source document without the file extension."
    )
    filepath: str | None = Field(
        default=None, description="The full absolute path to the local source file."
    )
    answer: str | None = Field(
        description="The generated AI response based on the retrieved context. Should be accurate and concise."
    )
