from graxon.projects.types import ProjectCreateParams, ProjectResponseParams
from graxon.project_configs.types import ProjectConfigCreateParams
from graxon.client import GraxonAsyncClient
import asyncio
import uuid


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    org_id = "test"
    # project_id: uuid.UUID = uuid.UUID("e123f25c-a135-4990-9ff3-68561ae55bf5")

    llm_model_id: uuid.UUID = uuid.UUID("713c1e08-6739-4d8a-b33c-786ca896a219")
    llm_model_credential_id: uuid.UUID = uuid.UUID("e432613d-55d2-48c6-87e2-cdd148cfa27d")

    embedding_model_id: uuid.UUID = uuid.UUID("cea2db34-9fa7-4ce7-aa48-9feb4c0c801c",)
    embedding_model_credential_id: uuid.UUID = uuid.UUID("8a6212d6-6a3f-4de1-8df2-9e2e52519a13")

    sparse_text_model_id: uuid.UUID = uuid.UUID("91077ca9-ee08-4ae1-b80b-193d8451c9c5")
    sparse_text_model_credential_id: uuid.UUID = uuid.UUID("aea0a0bb-64bf-4434-8f05-4df2d9f5fced")

    reranker_model_id: uuid.UUID = uuid.UUID("514618b6-2748-457e-8c28-cb8eaf935043")
    reranker_model_credential_id: uuid.UUID = uuid.UUID("dc631edb-6e4b-464a-b6a3-79b55f84d0a3")

    ocr_model_id: uuid.UUID = uuid.UUID("862fcfc3-24a3-4967-a35c-88044dae1cb8")
    ocr_model_credential_id: uuid.UUID = uuid.UUID("abff39aa-3730-45b3-a3a7-85ec0d11e178")

    audio_model_id: uuid.UUID = uuid.UUID("27007f53-9fa8-4a72-aff1-4028feb9d61d")
    audio_model_credential_id: uuid.UUID = uuid.UUID("7849d7eb-ace9-4a08-b5f9-a12537c1c96b")

    video_model_id: uuid.UUID = uuid.UUID("6e23df10-11d4-4d63-a128-6577dfb45d1e")
    video_model_credential_id: uuid.UUID = uuid.UUID("5709ed71-29d0-4ae2-9020-fa4e12060a88")

    project_config = ProjectConfigCreateParams(
        graph_db_enable=True,
        sparse_embedding_enable=True,
        reranker_enable=True,
        llm_tag_extraction_enable=True,
        llm_model_id=llm_model_id,
        llm_model_credential_id=llm_model_credential_id,
        embedding_model_id=embedding_model_id,
        embedding_model_credential_id=embedding_model_credential_id,
        sparse_text_model_id=sparse_text_model_id,
        sparse_text_model_credential_id=sparse_text_model_credential_id,
        reranker_model_id=reranker_model_id,
        reranker_model_credential_id=reranker_model_credential_id,
        ocr_model_id=ocr_model_id,
        ocr_model_credential_id=ocr_model_credential_id,
        audio_model_id=audio_model_id,
        audio_model_credential_id=audio_model_credential_id,
        video_model_id=video_model_id,
        video_model_credential_id=video_model_credential_id
    )

    create_response = await client.projects.create(org_id=org_id, request=ProjectCreateParams(
        org_id=org_id,
        name="Test Project",
        description="Test Project Description",
        config=project_config,
        project_metadata={"key": "value"}
    ))

    print("\ncreate_response", create_response)

    get_response = await client.projects.get(org_id=org_id, project_id=create_response.id)

    print("\nget_response", get_response)

    list_response = await client.projects.list(org_id=org_id)

    print("\nlist_response", list_response)

    # delete_response = await client.projects.delete(org_id=org_id, project_id=create_response.id)

    # print("\ndelete_response", delete_response)

asyncio.run(main())
