from urllib.parse import quote

import httpx

from yoklama.base import Module
from yoklama.checkers import Checker, StatusCodeChecker


class InstelaChecker(Checker):
    def check(self, response: httpx.Response) -> bool:
        return "/user/" in str(response.url)


class Instela(Module):
    name = "tr.instela.com"
    url = "https://tr.instela.com/search?q=%40{value}&source=enter"
    checkers = [StatusCodeChecker(code=200), InstelaChecker()]

    def get_value(self) -> str:
        return quote(self.value.strip())
