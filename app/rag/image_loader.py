# app/rag/image_loader.py

import base64
from openai import OpenAI
from langchain_core.documents import Document

from app.core.config import settings


class ImageLoaderService:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def load(self, upload_file):
        """
        Convert uploaded image into rich text using OpenAI Vision.
        Then return LangChain Document for vector DB ingestion.
        """

        image_bytes = upload_file.file.read()

        encoded = base64.b64encode(
            image_bytes
        ).decode("utf-8")

        mime_type = (
            upload_file.content_type
            if upload_file.content_type
            else "image/jpeg"
        )

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """
Analyze this uploaded image carefully.

Return output in this format:

VISIBLE_TEXT:
Extract every visible word, number,
label, heading exactly.

IMAGE_DESCRIPTION:
Describe what objects, products,
people, logos, scenery or items
are present.

BUSINESS_CONTEXT:
Explain what this image may represent
(invoice, receipt, product ad,
screenshot, chart, form, ID card,
menu, presentation etc.)

KEY_DETAILS:
Mention important names, dates,
prices, values, measurements,
brand names, model names.

SUMMARY:
Give concise overall meaning.

If no text exists, still describe
the image clearly.
"""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime_type};base64,{encoded}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1600
        )

        text = response.choices[0].message.content

        # Optional debug print
        print("\n===== IMAGE OCR OUTPUT =====")
        print(text)
        print("============================\n")

        return [
            Document(
                page_content=text,
                metadata={
                    "source": upload_file.filename,
                    "type": "image",
                    "mime_type": mime_type
                }
            )
        ]