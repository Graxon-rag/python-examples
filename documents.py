from graxon.client import GraxonAsyncClient
import asyncio
import logging
import uuid

# Configure logging to show INFO level messages in the console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    org_id = "test"
    project_id: uuid.UUID = uuid.UUID("e538c04e-22c0-41a4-a1f6-49b91183e0bb")

    file_path = "./test_data/youtube_podcast_video.mp4"
    # file_path = "./test_data/large.pdf"
    # file_path = "./test_data/Test file 1.pdf"

    upload_response = await client.documents.upload(
        org_id=org_id,
        project_id=project_id,
        file_path=file_path,
        chunk_size_in_mb=15,
    )

    print("\nUpload", upload_response)

    print("\n********************************\n")

    get_response = await client.documents.get(org_id=org_id, project_id=project_id, document_id=upload_response.document_id)

    print("\nGet", get_response)

    print("\n********************************\n")

    signed_url = await client.documents.get_signed_url(org_id=org_id, project_id=project_id, bucket=get_response.bucket, key=get_response.key)

    print("\nSigned URL", signed_url)

    print("\n********************************\n")

    # process_response = await client.documents.process(org_id=org_id, project_id=project_id, document_id=upload_response.document_id)

    # print("\nProcess", process_response)

    # print("\n********************************\n")

    list_response = await client.documents.list(org_id=org_id, project_id=project_id)

    print("\nList", list_response)

    print("\n********************************\n")

    delete_response = await client.documents.delete(org_id=org_id, project_id=project_id, document_id=upload_response.document_id)

    print("\nDelete", delete_response)


asyncio.run(main())
