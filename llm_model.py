from graxon.llm_models.types import LLMModelCreateParams, LLMModelProvider
from graxon.client import GraxonAsyncClient
import asyncio


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    org_id = "test"

    # create llm model
    create_response = await client.llm_models.create(org_id, request=LLMModelCreateParams(
        org_id=org_id,
        name="OpenAI Test Model",
        model_name="text-davinci-003",
        model_id="text-davinci-003",
        provider=LLMModelProvider.OPENAI,
        description="OpenAI Test Model"
    ))

    print("\ncreate_response", create_response)

    # Create Multiple LLM Models
    multiple_create_response = await client.llm_models.create_multiple(org_id, [
        LLMModelCreateParams(
            org_id=org_id,
            name="DEEPSEEKTest Model",
            model_name="DEEPSEEK Chat",
            model_id="deepseek-chat",
            provider=LLMModelProvider.DEEPSEEK,
            description="DEEPSEEK Test Model"
        ),
        LLMModelCreateParams(
            org_id=org_id,
            name="GEMINI Test Model",
            model_name="gemini 2.5 pro",
            model_id="gemini-2.5-pro",
            provider=LLMModelProvider.GEMINI,
            description="GEMINI Test Model"
        )
    ])

    print("\nmultiple_create_response", multiple_create_response)

    # Get LLM Model
    get_response = await client.llm_models.get(org_id, create_response.id)

    print("\nget_response", get_response)

    # List LLM Models by Provider
    list_response = await client.llm_models.list_by_provider(org_id, LLMModelProvider.OPENAI)

    print("\nlist_response", list_response)

    # Delete LLM Model
    delete_response = await client.llm_models.delete(org_id, create_response.id)

    print("\ndelete_response", delete_response)

asyncio.run(main())
