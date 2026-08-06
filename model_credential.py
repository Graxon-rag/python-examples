from graxon.model_credentials.types import ModelCredentialCreateParams
from graxon.types import ModelProvider
from graxon.client import GraxonAsyncClient
import asyncio


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    org_id = "test"

    # Create
    create_response = await client.model_credentials.create(org_id=org_id, request=ModelCredentialCreateParams(
        org_id=org_id,
        name="Deepseek Api Key",
        description="Deepseek Api Key",
        provider=ModelProvider.DEEPSEEK,
        api_key="deepseek_api_key"
    ))

    print("Create", create_response)

    # Get
    get_response = await client.model_credentials.get(org_id=org_id, model_credential_id=create_response.id)

    print("Get", get_response)

    # List By Provider
    list_response = await client.model_credentials.list_by_provider(org_id=org_id, provider=ModelProvider.DEEPSEEK)

    print("List", list_response)

    delete_response = await client.model_credentials.delete(org_id=org_id, model_credential_id=create_response.id)

    print("Delete", delete_response)

asyncio.run(main())
