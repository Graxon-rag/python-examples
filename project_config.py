from graxon.project_configs.types import ProjectConfigUpdateParams, ProjectConfigGetParams
from graxon.client import GraxonAsyncClient
import asyncio
import uuid


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    org_id = "test"
    project_id: uuid.UUID = uuid.UUID("e538c04e-22c0-41a4-a1f6-49b91183e0bb")
    config_id: uuid.UUID = uuid.UUID("6f3121ef-68d0-4ab5-80d5-973ceb3a6b1a")

    get_response = await client.project_configs.get(
        org_id=org_id,
        project_id=project_id,
        config_id=config_id,
    )

    print("Get", get_response)
    print("\n*********************************************\n")

    updated_llm_model_id: uuid.UUID = uuid.UUID("1658848a-47c2-4900-a3d1-dea27223587d")
    updated_llm_model_credential_id: uuid.UUID = uuid.UUID("8a6212d6-6a3f-4de1-8df2-9e2e52519a13")

    update_response = await client.project_configs.update(
        org_id=org_id,
        project_id=project_id,
        config_id=config_id,
        update=ProjectConfigUpdateParams(
           llm_model_id=updated_llm_model_id,
           llm_model_credential_id=updated_llm_model_credential_id
           # more .....
        ),
    )

    print("\nUpdate", update_response)

asyncio.run(main())
