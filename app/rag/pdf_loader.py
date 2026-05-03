# app/rag/pdf_loader.py

import tempfile
import os
from langchain_community.document_loaders import PyPDFLoader


class PDFLoaderService:

    def load(self, upload_file):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(upload_file.file.read())
            temp_path = tmp.name

        try:
            loader = PyPDFLoader(temp_path)
            docs = loader.load()
            return docs

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)