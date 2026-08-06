from graxon.client import GraxonAsyncClient
import asyncio


async def main():
    base_url = "http://localhost:8888"
    api_key = "graxon_api_key"
    timeout = 60
    client = GraxonAsyncClient(api_key=api_key, base_url=base_url, timeout=timeout)

    # list all
    all = await client.model_providers.all_models()
    print("All", all)

    # llm models
    llm = await client.model_providers.llm_models()
    print("LLM", llm)

    # embedding models
    embedding = await client.model_providers.embedding_models()
    print("Embedding", embedding)

    # sparse models
    sparse = await client.model_providers.sparse_models()
    print("Sparse", sparse)

    # reranker models
    reranker = await client.model_providers.reranker_models()
    print("Reranker", reranker)

    # audio models
    audio = await client.model_providers.audio_models()
    print("Audio", audio)

    # video models
    video = await client.model_providers.video_models()
    print("Video", video)

    # ocr models
    ocr = await client.model_providers.ocr_models()
    print("OCR", ocr)

asyncio.run(main())
