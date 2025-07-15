from typing import Optional

from agno.embedder.ollama import OllamaEmbedder
from agno.vectordb.chroma import ChromaDb
from agno.vectordb.milvus import Milvus
from pydantic import BaseModel

# from pymilvus import connections, utility
#
# connections.connect()
# if utility.has_collection("recipies"):
#     utility.drop_collection("recipies")


class VectorDBConfig(BaseModel):
    db_type: str  # Type of the vector DB (e.g., "faiss", "pinecone")
    index_name: str  # Index name in the vector DB
    api_key: Optional[str] = None  # API key if needed
    host: Optional[str] = None  # Host URL if needed
    port: Optional[int] = None  # Port if needed


class VectorDb:
    def __init__(self, config: VectorDBConfig):
        self.config = config
        self.db = self._get_db_client()

    def _get_db_client(self):
        """
        Factory method to return the appropriate vector DB client based on config.
        """
        if self.config.db_type == 'chroma':
            return self._initialise_chroma()
        elif self.config.db_type == 'milvus':
            return self._initialise_milvus()
        else:
            raise ValueError(f"Unsupported vector DB type: {self.config.db_type}")

    def _initialise_chroma(self):
        """
        Initialize and return chrome client instance.
        """
        embedding_model = OllamaEmbedder(id='mxbai-embed-large', dimensions=1024)
        vector_store = ChromaDb(
            collection=self.config.index_name,
            embedder=embedding_model,
            persistent_client=True
        )
        return vector_store

    def _initialise_milvus(self):

        vector_db = Milvus(
            collection=self.config.index_name or "recipies",
            embedder=OllamaEmbedder(id='mxbai-embed-large', dimensions=1024)

        )

        return vector_db
