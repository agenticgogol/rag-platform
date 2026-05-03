# app/core/constants.py

APP_NAME = "RAG Platform"
APP_VERSION = "1.0.0"

# API Paths
HEALTH_ENDPOINT = "/health"
ASK_ENDPOINT = "/ask"
UPLOAD_PDF_ENDPOINT = "/upload-pdf"
UPLOAD_URL_ENDPOINT = "/upload-url"

# RAG Defaults
DEFAULT_TOP_K = 4
DEFAULT_CHUNK_SIZE = 800
DEFAULT_CHUNK_OVERLAP = 150
MAX_URLS_PER_REQUEST = 20
MAX_PDFS_PER_REQUEST = 10

# LLM Defaults
DEFAULT_TEMPERATURE = 0
DEFAULT_MODEL = "gpt-4o-mini"

# Timeouts
REQUEST_TIMEOUT_SECONDS = 60

# Logging
LOG_LEVEL = "INFO"

# Prompt Template
RAG_PROMPT_TEMPLATE = """
You are a helpful enterprise assistant.

Use ONLY the provided context.
If answer is not found, say:
"I could not find that information in the uploaded knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""