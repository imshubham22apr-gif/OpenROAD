import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_key_here")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
    VECTOR_DB = os.getenv("VECTOR_DB", "chroma")
    PERSIST_DIRECTORY = os.getenv("PERSIST_DIRECTORY", "backend/db/")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "chipathon_docs")
    DOCS_PATH = os.getenv("DOCS_PATH", "frontend/docs/")
