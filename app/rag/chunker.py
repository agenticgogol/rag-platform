# app/rag/chunker.py

from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import settings


class ChunkingService:

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

    def split(self, docs):
        return self.splitter.split_documents(docs)