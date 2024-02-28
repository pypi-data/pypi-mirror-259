import os

from komodo.shared.utils.lambda_api import lambda_fetch_openai_api_key
from langchain_community.embeddings import OpenAIEmbeddings


def get_embeddings() -> OpenAIEmbeddings:
    if 'OPENAI_API_KEY' not in os.environ:
        os.environ['OPENAI_API_KEY'] = lambda_fetch_openai_api_key()
    return OpenAIEmbeddings()
