from graxon.orgs.types import OrganizationCreateParams, OrganizationResponseParams
from graxon.client import GraxonAsyncClient
import asyncio


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    # Create Org
    create_response = await client.orgs.create(request=OrganizationCreateParams(name="test", description="test org"))

    print(create_response)

    # Get Org
    response = await client.orgs.get(org_id=create_response.id)

    print(response)

    # List Orgs
    response = await client.orgs.list()

    print(response)

    # Delete Org
    delete_result = await client.orgs.delete(org_id=create_response.id)

    print(delete_result)

asyncio.run(main())
