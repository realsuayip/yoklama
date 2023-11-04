import asyncio

import httpx

from yoklama.base import AVAILABLE_MODULES


async def run(value: str) -> None:
    client = httpx.AsyncClient(follow_redirects=True, timeout=30)

    futures = []
    for klass in AVAILABLE_MODULES:
        instance = klass(client=client)
        instance(value=value)
        futures.append(instance.run())

    await asyncio.gather(*futures)
    await client.aclose()
