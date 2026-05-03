# app/schemas/response.py

from pydantic import BaseModel
from typing import Optional, List


class MessageResponse(BaseModel):
    message: str


class AskResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = None


class HealthResponse(BaseModel):
    status: str