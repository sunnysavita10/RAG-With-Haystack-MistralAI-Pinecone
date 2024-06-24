from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

print("Import Successfully")

# Wrapper class for the API key


class ApiKeyWrapper:
    def __init__(self, api_key):
        self.api_key = api_key

    def resolve_value(self):
        return self.api_key


def pinecone_config():
    wrapped_api_key = ApiKeyWrapper(os.environ['PINECONE_API_KEY'])

    document_store = PineconeDocumentStore(
        api_key=wrapped_api_key,
        index="default",
        namespace="default",
        dimension=768
    )
    return document_store
