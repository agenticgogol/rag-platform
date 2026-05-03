# app/rag/llm.py

from langchain_openai import ChatOpenAI
from app.core.config import settings


def get_llm():

    return ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE
    )