import os
import glob
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from backend.config import Config
from backend.rag.utils import log_info, log_error

def ingest_docs():
    log_info("Starting document ingestion...")
    
    try:
        # 1. Load markdown files
        docs_path = Config.DOCS_PATH
        if not os.path.exists(docs_path):
            log_error(f"Docs path {docs_path} does not exist.")
            return

        loader = DirectoryLoader(docs_path, glob="**/*.md", loader_cls=TextLoader)
        documents = loader.load()
        log_info(f"Loaded {len(documents)} documents.")

        if not documents:
            log_error("No documents found to ingest.")
            return

        # 2. Chunk text
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        chunks = text_splitter.split_documents(documents)
        log_info(f"Split documents into {len(chunks)} chunks.")

        # 3. Generate embeddings and store in Vector DB
        embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            openai_api_key=Config.OPENAI_API_KEY
        )

        log_info(f"Storing chunks in {Config.VECTOR_DB}...")
        
        persist_dir = Config.PERSIST_DIRECTORY
        if not os.path.exists(persist_dir):
            os.makedirs(persist_dir)

        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=persist_dir,
            collection_name=Config.COLLECTION_NAME
        )
        
        # Persist the database
        vector_db.persist()
        log_info("Ingestion completed successfully and persisted.")

    except Exception as e:
        log_error(f"Ingestion failed: {str(e)}")

if __name__ == "__main__":
    ingest_docs()
