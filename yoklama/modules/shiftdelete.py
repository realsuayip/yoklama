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

from urllib.parse import urljoin

from bs4 import BeautifulSoup

from yoklama.base import DEFAULT_USER_AGENT, Module


class ShiftDelete(Module):
    name = "shiftdelete.net"
    url = "https://forum.shiftdelete.net/ara/search"

    token_url = "https://forum.shiftdelete.net/ara/"
    base_url = "https://forum.shiftdelete.net/"

    async def check(self) -> bool:
        # TODO: Add test
        token_response = await self.client.get("https://forum.shiftdelete.net/ara/")

        if not token_response.is_success:
            return False

        soup = BeautifulSoup(token_response.text, "html.parser")
        elem = soup.select_one("input[name=_xfToken]")
        token = elem.get("value")

        response = await self.client.post(
            self.url,
            headers={"Referer": self.url, "User-Agent": DEFAULT_USER_AGENT},
            data={
                "_xfResponseType": "json",
                "_xfToken": token,
                "c[users]": self.get_value(),
            },
            cookies={"xf_csrf": "1"},
        )

        if not response.is_success:
            return False

        data = response.json()
        status, redirect = data["status"], data.get("redirect")

        if (status != "ok") or (not redirect):
            return False

        profile = await self.client.get(data["redirect"])
        soup = BeautifulSoup(profile.text, "html.parser")
        elem = soup.select_one("a.username[data-user-id]")
        profile_url = urljoin(self.base_url, elem.get("href"))
        self.response_url = profile_url
        return True

    def get_value(self) -> str:
        return self.value.strip()
