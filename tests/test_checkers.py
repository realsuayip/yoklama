"""
Copyright (c) 2023-2024, Şuayip Üzülmez, and contributors

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
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
