# app/core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # App
    # =========================
    APP_ENV: str = "dev"
    APP_NAME: str = "RAG Platform"
    APP_PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    # =========================
    # OpenAI / LLM
    # =========================
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-4o-mini"
    TEMPERATURE: float = 0.0

    # Optional alternate providers
    GROQ_API_KEY: str = ""
    USE_GROQ: bool = False

    # =========================
    # Qdrant
    # =========================
    QDRANT_URL: str
    QDRANT_API_KEY: str
    COLLECTION_NAME: str = "rag_docs"

    # =========================
    # RAG Parameters
    # =========================
    TOP_K: int = 4
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150

    # =========================
    # Frontend / Internal URLs
    # =========================
    BACKEND_URL: str = "http://backend-service:8000"

    # =========================
    # Observability
    # =========================
    LANGCHAIN_TRACING_V2: bool = False
    LANGCHAIN_API_KEY: str = ""
    LANGCHAIN_PROJECT: str = "rag-platform"

    # =========================
    # Security
    # =========================
    ENABLE_AUTH: bool = False
    JWT_SECRET_KEY: str = "change_me"

    # =========================
    # Pydantic Settings
    # =========================
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )


settings = Settings()