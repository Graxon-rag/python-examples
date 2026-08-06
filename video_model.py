from graxon.video_models.types import (
    VideoModelCreateParams,
    VideoModelProvider,
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

    # Create Video Model
    create_response = await client.video_models.create(
        org_id,
        request=VideoModelCreateParams(
            org_id=org_id,
            name="TwelveLabs Test Model",
            provider=VideoModelProvider.TWELVELABS,
            model_name="TwelveLabs Video Model",
            model_id="twelvelabs-video",
            description="TwelveLabs Video Test Model",
        ),
    )

    print("\ncreate_response", create_response)

    # Create Multiple Video Models
    multiple_create_response = await client.video_models.create_multiple(
        org_id,
        [
            VideoModelCreateParams(
                org_id=org_id,
                name="Gemini Video Test Model",
                provider=VideoModelProvider.GEMINI,
                model_name="Gemini Video",
                model_id="gemini-video",
                description="Gemini Video Test Model",
            ),
            VideoModelCreateParams(
                org_id=org_id,
                name="TwelveLabs Test Model 2",
                provider=VideoModelProvider.TWELVELABS,
                model_name="TwelveLabs Video Model 2",
                model_id="twelvelabs-video-2",
                description="TwelveLabs Video Test Model 2",
            ),
        ],
    )

    print("\nmultiple_create_response", multiple_create_response)

    # Get Video Model
    get_response = await client.video_models.get(
        org_id,
        create_response.id,
    )

    print("\nget_response", get_response)

    # List Video Models by Provider
    list_response = await client.video_models.list_by_provider(
        org_id,
        VideoModelProvider.TWELVELABS,
    )

    print("\nlist_response", list_response)

    # Delete Video Model
    delete_response = await client.video_models.delete(
        org_id,
        create_response.id,
    )

    print("\ndelete_response", delete_response)


asyncio.run(main())
