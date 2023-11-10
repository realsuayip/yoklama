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
