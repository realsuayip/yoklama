from collections.abc import AsyncIterator

import httpx
import pytest_asyncio


@pytest_asyncio.fixture
async def httpx_client() -> AsyncIterator[httpx.AsyncClient]:
    client = httpx.AsyncClient()
    try:
        yield client
    finally:
        await client.aclose()
