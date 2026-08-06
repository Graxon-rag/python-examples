from graxon.audio_models.types import AudioModelCreateParams, AudioModelProvider
from graxon.client import GraxonAsyncClient
import asyncio


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    org_id = "test"

    # create audio model
    create_response = await client.audio_models.create(org_id, request=AudioModelCreateParams(
        org_id=org_id,
        name="Deepgram Test Model",
        model_name="en-US_BroadbandModel Test Model",
        model_id="en-US_BroadbandModel",
        provider=AudioModelProvider.DEEPGRAM,
        description="Deepgram Test Model"
    ))

    print(create_response)

    # create multiple audio models
    multiple_create_response = await client.audio_models.create_multiple(org_id, [
        AudioModelCreateParams(
            org_id=org_id,
            name="ELEVENLABS Test Model",
            model_name="en-ELEVENLABS Test Model",
            model_id="en-ELEVENLABS",
            provider=AudioModelProvider.ELEVENLABS,
            description="ELEVENLABS Test Model"
        ),
        AudioModelCreateParams(
            org_id=org_id,
            name="ASSEMBLYAI Test Model",
            model_name="en-ASSEMBLYAI Test Model",
            model_id="en-ASSEMBLYAI",
            provider=AudioModelProvider.ASSEMBLYAI,
            description="ASSEMBLYAI Test Model"
        )
    ])

    print(multiple_create_response)

    # get audio model
    get_response = await client.audio_models.get(org_id, audio_model_id=create_response.id)

    print(get_response)

    # list by provider
    list_response = await client.audio_models.list_by_provider(org_id, provider=AudioModelProvider.DEEPGRAM)

    print(list_response)

    # delete audio model
    delete_response = await client.audio_models.delete(org_id, audio_model_id=create_response.id)

    print(delete_response)


asyncio.run(main())
