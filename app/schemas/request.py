# app/schemas/request.py

from pydantic import BaseModel, HttpUrl, Field, field_validator
from typing import List


class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=2,
        max_length=2000,
        examples=["What is the refund policy?"]
    )

    @field_validator("question")
    @classmethod
    def clean_question(cls, v: str):
        return v.strip()


class URLUploadRequest(BaseModel):
    urls: List[HttpUrl] = Field(
        ...,
        min_length=1,
        max_length=20,
        examples=[["https://example.com", "https://docs.python.org"]]
    )