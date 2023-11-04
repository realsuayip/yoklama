import asyncio

import httpx

from yoklama.base import AVAILABLE_MODULES


async def run(value: str) -> None:
    print("Received: '%s'" % value)
    client = httpx.AsyncClient(follow_redirects=True, timeout=30)

    futures = []
    for klass in AVAILABLE_MODULES:
        instance = klass(client=client)
        instance(value=value)
        futures.append(instance.run())

    for coro in asyncio.as_completed(futures):
        result = await coro
        if result is not None:
            print("\033[1m%s\033[0m — %s" % result)
    await client.aclose()
