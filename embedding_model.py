from graxon.embedding_models.types import EmbeddingModelCreateParams, EmbeddingModelProvider
from graxon.client import GraxonAsyncClient
import asyncio


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    org_id = "test"

    # create embedding model
    create_response = await client.embedding_models.create(org_id, request=EmbeddingModelCreateParams(
        org_id=org_id,
        name="OpenAI Test Model",
        model_name="text-embedding-ada-002",
        model_id="text-embedding-ada-002",
        provider=EmbeddingModelProvider.OPENAI,
        dimension=1536,
        description="OpenAI Test Model"
    ))

    print("\ncreate_response", create_response)

    # Create Multiple Embedding Models
    multiple_create_response = await client.embedding_models.create_multiple(org_id, [
        EmbeddingModelCreateParams(
            org_id=org_id,
            name="GEMINI Test Model",
            model_name="text-embedding-001 Model",
            model_id="text-embedding-001",
            provider=EmbeddingModelProvider.GEMINI,
            dimension=1536,
            description="GEMINI Test Model"
        ),
        EmbeddingModelCreateParams(
            org_id=org_id,
            name="VOYAGE Test Model",
            model_name="embedding VOYAGE",
            model_id="voyage-4-large",
            provider=EmbeddingModelProvider.VOYAGE,
            dimension=1536,
            description="VOYAGE Test Model"
        )
    ])

    print("\nmultiple_create_response", multiple_create_response)

    # Get
    get_response = await client.embedding_models.get(org_id=org_id, embedding_model_id=create_response.id)

    print("\nget_response", get_response)

    # List By Provider
    list_response = await client.embedding_models.list_by_provider(org_id=org_id, provider=EmbeddingModelProvider.OPENAI)

    print("\nlist_response", list_response)

    # Delete
    delete_response = await client.embedding_models.delete(org_id=org_id, embedding_model_id=create_response.id)

    print("\ndelete_response", delete_response)

asyncio.run(main())
