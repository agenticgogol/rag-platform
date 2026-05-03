# app/rag/vectorstore.py

from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from app.core.config import settings
from app.rag.embeddings import get_embeddings


class VectorStoreService:

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )

        self._create_collection_if_missing()

        self.db = QdrantVectorStore(
            client=self.client,
            collection_name=settings.COLLECTION_NAME,
            embedding=get_embeddings()
        )

    def _create_collection_if_missing(self):

        collections = self.client.get_collections().collections
        names = [collection.name for collection in collections]

        if settings.COLLECTION_NAME not in names:

            self.client.create_collection(
                collection_name=settings.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=1536,
                    distance=Distance.COSINE
                )
            )

    def add_documents(self, docs):
        self.db.add_documents(docs)

    def search(self, question, k):
        return self.db.similarity_search(question, k=k)