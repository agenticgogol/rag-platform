# app/rag/url_loader.py

from langchain_community.document_loaders import WebBaseLoader


class URLLoaderService:

    def load(self, url: str):
        """
        Load content from a website URL.
        """

        loader = WebBaseLoader(
            web_paths=[str(url)],
            requests_kwargs={
                "headers": {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
                },
                "timeout": 20
            }
        )

        docs = loader.load()

        return docs