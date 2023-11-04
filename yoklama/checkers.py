from typing import Any

import httpx
from bs4 import BeautifulSoup


class Checker:
    def check(self, response: httpx.Response) -> bool:
        raise NotImplementedError


class StatusCodeChecker(Checker):
    def __init__(self, *, code: int) -> None:
        self.code = code

    def check(self, response: httpx.Response) -> bool:
        return response.status_code == self.code


class HTMLContentsChecker(Checker):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.args = args
        self.kwargs = kwargs

    def check(self, response: httpx.Response) -> bool:
        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.find(*self.args, **self.kwargs)
        return elements is not None
