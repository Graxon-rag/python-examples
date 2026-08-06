from graxon.sparse_models.types import (
    SparseModelCreateParams,
    SparseModelProvider,
    SparseModelProviderType,
)
from graxon.client import GraxonAsyncClient
import asyncio


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60

    client = GraxonAsyncClient(
        api_key=api_key,
        base_url=base_url,
        timeout=timeout,
    )

    org_id = "test"

    # Create Sparse Text Model
    create_response = await client.sparse_models.create(
        org_id,
        request=SparseModelCreateParams(
            org_id=org_id,
            name="Pinecone Sparse Test Model",
            provider_type=SparseModelProviderType.CLOUD,
            provider=SparseModelProvider.PINECONE,
            model_name="Pinecone Sparse English",
            model_id="pinecone-sparse-english-v0",
            description="Pinecone Sparse Text Test Model",
            size_in_gb=0.0,
        ),
    )

    print("\ncreate_response", create_response)

    # Create Multiple Sparse Text Models
    multiple_create_response = await client.sparse_models.create_multiple(
        org_id,
        [
            SparseModelCreateParams(
                org_id=org_id,
                name="Qdrant Sparse Test Model",
                provider_type=SparseModelProviderType.CLOUD,
                provider=SparseModelProvider.QDRANT,
                model_name="Qdrant Sparse",
                model_id="qdrant-sparse",
                description="Qdrant Sparse Text Test Model",
                size_in_gb=0.0,
            ),
            SparseModelCreateParams(
                org_id=org_id,
                name="Prithvida Sparse Test Model",
                provider_type=SparseModelProviderType.LOCAL,
                provider=SparseModelProvider.PRITHVIDA,
                model_name="Prithvida Sparse",
                model_id="prithvida-sparse",
                description="Prithvida Local Sparse Text Test Model",
                size_in_gb=0.5,
            ),
        ],
    )

    print("\nmultiple_create_response", multiple_create_response)

    # Get Sparse Text Model
    get_response = await client.sparse_models.get(
        org_id,
        create_response.id,
    )

    print("\nget_response", get_response)

    # List Sparse
    list_response = await client.sparse_models.list(
        org_id,
    )

    print("\nlist_response", list_response)

    # Delete Sparse Text Model
    delete_response = await client.sparse_models.delete(
        org_id,
        create_response.id,
    )

    print("\ndelete_response", delete_response)


asyncio.run(main())
