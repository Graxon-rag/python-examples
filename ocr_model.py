from graxon.ocr_models.types import OCRModelCreateParams, OCRModelProvider
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

    # Create OCR Model
    create_response = await client.ocr_models.create(
        org_id,
        request=OCRModelCreateParams(
            org_id=org_id,
            name="Datalab Test Model",
            provider=OCRModelProvider.DATALAB,
            model_name="Datalab OCR",
            model_id="datalab-ocr",
            description="Datalab OCR Test Model",
        ),
    )

    print("\ncreate_response", create_response)

    # Create Multiple OCR Models
    multiple_create_response = await client.ocr_models.create_multiple(
        org_id,
        [
            OCRModelCreateParams(
                org_id=org_id,
                name="Mistral OCR Test Model",
                provider=OCRModelProvider.MISTRAL,
                model_name="Mistral OCR",
                model_id="mistral-ocr-latest",
                description="Mistral OCR Test Model",
            ),
            OCRModelCreateParams(
                org_id=org_id,
                name="LlamaParse Test Model",
                provider=OCRModelProvider.LLAMAPARSE,
                model_name="LlamaParse",
                model_id="llamaparse",
                description="LlamaParse OCR Test Model",
            ),
        ],
    )

    print("\nmultiple_create_response", multiple_create_response)

    # Get OCR Model
    get_response = await client.ocr_models.get(
        org_id,
        create_response.id,
    )

    print("\nget_response", get_response)

    # List OCR Models by Provider
    list_response = await client.ocr_models.list_by_provider(
        org_id,
        OCRModelProvider.DATALAB,
    )

    print("\nlist_response", list_response)

    # Delete OCR Model
    delete_response = await client.ocr_models.delete(
        org_id,
        create_response.id,
    )

    print("\ndelete_response", delete_response)


asyncio.run(main())
