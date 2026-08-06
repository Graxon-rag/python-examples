from graxon.client import GraxonAsyncClient
from graxon.webhooks.types import WebhookCreateParams
import asyncio
import uuid


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
    project_id: uuid.UUID = uuid.UUID("ba512d16-bbfa-459b-b684-32e8996fd08c")

    # Create
    create_response = await client.webhooks.create(
        org_id,
        project_id,
        request=WebhookCreateParams(
            org_id=org_id,
            project_id=project_id,
            name="test",
            url="http://localhost:8080/webhooks/graxon",
            token="xxxxxxxxxxxxxxxxxxx",
        ),
    )

    print("\ncreate_response", create_response)

    # Get
    get_response = await client.webhooks.get(org_id, project_id, webhook_id=create_response.id)

    print("\nget_response", get_response)

    # List
    list_response = await client.webhooks.list(org_id, project_id)

    print("\nlist_response", list_response)

    # Delete
    delete_response = await client.webhooks.delete(org_id, project_id, webhook_id=create_response.id)

    print("\ndelete_response", delete_response)

asyncio.run(main())
