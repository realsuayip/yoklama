import httpx
import pytest
from httpx import AsyncClient
from pytest_httpx import HTTPXMock

from yoklama.modules.eksisozluk import EksiSozluk
from yoklama.modules.instela import Instela
from yoklama.modules.uludagsozluk import UludagSozluk


@pytest.mark.asyncio
async def test_status_code_checker(
    httpx_client: AsyncClient, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(status_code=200)
    httpx_mock.add_response(status_code=404)

    # Using a module that uses this checker.
    module = EksiSozluk(client=httpx_client)
    module(value="username")

    name, url = await module.run()  # type: ignore[misc]
    not_found = await module.run()

    assert name == "eksisozluk.com"
    assert str(url) == "https://eksisozluk.com/biri/username"
    assert not_found is None


@pytest.mark.asyncio
async def test_html_contents_checker(
    httpx_client: AsyncClient, httpx_mock: HTTPXMock
) -> None:
    httpx_mock.add_response(status_code=200, text="<div class='user-menu p-5'></div>")
    httpx_mock.add_response(status_code=200, text="<div class='something-else'></div>")

    # Using a module that uses this checker.
    module = UludagSozluk(client=httpx_client)
    module(value="username")

    name, url = await module.run()  # type: ignore[misc]
    not_found = await module.run()

    assert name == "uludagsozluk.com"
    assert str(url) == "https://www.uludagsozluk.com/username"
    assert not_found is None


@pytest.mark.asyncio
async def test_instela_checker(
    httpx_client: AsyncClient, httpx_mock: HTTPXMock
) -> None:
    def found_response(request: httpx.Request) -> httpx.Response:
        request.url = httpx.URL("https://tr.instela.com/user/username-123456")
        return httpx.Response(status_code=200, request=request)

    def not_found_response(request: httpx.Request) -> httpx.Response:
        request.url = httpx.URL("https://tr.instela.com/")
        return httpx.Response(status_code=200, request=request)

    httpx_mock.add_callback(found_response)
    httpx_mock.add_callback(not_found_response)

    # Using a module that uses this checker.
    module = Instela(client=httpx_client)
    module(value="username")

    name, url = await module.run()  # type: ignore[misc]
    not_found = await module.run()

    assert name == "tr.instela.com"
    assert str(url) == "https://tr.instela.com/user/username-123456"
    assert not_found is None
