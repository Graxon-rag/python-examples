from graxon.reranker_models.types import (
    RerankerModelCreateParams,
    RerankerModelProvider,
    RerankerModelProviderType,
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

    # Create Reranker Model
    create_response = await client.reranker_models.create(
        org_id,
        request=RerankerModelCreateParams(
            org_id=org_id,
            name="Jina Reranker Test Model",
            provider_type=RerankerModelProviderType.CLOUD,
            provider=RerankerModelProvider.JINA,
            model_name="Jina Reranker v2",
            model_id="jina-reranker-v2",
            description="Jina Reranker Test Model",
            size_in_gb=0.0,
        ),
    )

    print("\ncreate_response", create_response)

    # Create Multiple Reranker Models
    multiple_create_response = await client.reranker_models.create_multiple(
        org_id,
        [
            RerankerModelCreateParams(
                org_id=org_id,
                name="Cohere Reranker Test Model",
                provider_type=RerankerModelProviderType.CLOUD,
                provider=RerankerModelProvider.COHERE,
                model_name="Cohere Rerank",
                model_id="rerank-v3.5",
                description="Cohere Reranker Test Model",
                size_in_gb=0.0,
            ),
            RerankerModelCreateParams(
                org_id=org_id,
                name="Xenova Reranker Test Model",
                provider_type=RerankerModelProviderType.LOCAL,
                provider=RerankerModelProvider.XENOVA,
                model_name="Xenova Reranker",
                model_id="Xenova/ms-marco-MiniLM-L-6-v2",
                description="Xenova Local Reranker Test Model",
                size_in_gb=0.1,
            ),
        ],
    )

    print("\nmultiple_create_response", multiple_create_response)

    # Get Reranker Model
    get_response = await client.reranker_models.get(
        org_id,
        create_response.id,
    )

    print("\nget_response", get_response)

    # List Reranker 
    list_response = await client.reranker_models.list(
        org_id,
    )

    print("\nlist_response", list_response)

    # Delete Reranker Model
    delete_response = await client.reranker_models.delete(
        org_id,
        create_response.id,
    )

    print("\ndelete_response", delete_response)


asyncio.run(main())
