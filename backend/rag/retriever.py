import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from backend.config import Config
from backend.rag.utils import log_info, log_error

class Retriever:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            openai_api_key=Config.OPENAI_API_KEY
        )
        self.persist_dir = Config.PERSIST_DIRECTORY
        self.collection_name = Config.COLLECTION_NAME
        
        # Load Chroma DB
        try:
            self.vector_db = Chroma(
                persist_directory=self.persist_dir,
                embedding_function=self.embeddings,
                collection_name=self.collection_name
            )
            log_info("Retriever initialized successfully.")
        except Exception as e:
            log_error(f"Retriever initialization failed: {str(e)}")
            self.vector_db = None

    def get_context(self, query):
        if not self.vector_db:
            return None, []
        
        try:
            results = self.vector_db.similarity_search_with_score(query, k=3)
            
            context = ""
            sources = []
            for doc, score in results:
                content = doc.page_content
                source = os.path.basename(doc.metadata.get("source", "unknown"))
                context += f"\n---\nSource: {source}\n{content}\n"
                sources.append({
                    "content": content,
                    "source": source
                })
            
            return context, sources
        except Exception as e:
            log_error(f"Context retrieval failed: {str(e)}")
            return None, []
