from __future__ import annotations

import logging
from typing import Any, TypeVar

import httpx

from yoklama.checkers import Checker, StatusCodeChecker

logger = logging.getLogger(__name__)

AVAILABLE_MODULES: list[type[Module]] = []
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"
    " (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
)

Self = TypeVar("Self", bound="Module")


class Module:
    name: str
    url: str
    checkers: list[Checker] | None = None

    def __init__(self, *, client: httpx.AsyncClient) -> None:
        self.client = client
        self.response_url: httpx.URL | None = None

    def __init_subclass__(cls, enabled: bool = True) -> None:
        AVAILABLE_MODULES.append(cls)

    def __call__(self: Self, *, value: str) -> Self:
        self.value = value
        return self

    def __repr__(self) -> str:
        return "<Module %s>" % self.name

    async def get_response(self) -> httpx.Response:
        url, headers = self.get_url(), self.get_headers()
        return await self.client.get(url, headers=headers)

    async def check(self) -> bool:
        # TODO: Add a central mechanism to handle all sorts of errors.
        #  In that, aggregate checker exceptions/errors and network errors
        #  in an errors list in module instances.
        try:
            response = await self.get_response()
        except httpx.HTTPError:
            print("Network error in %s" % self.url)
            return False
        self.response_url = response.url
        return all(checker.check(response) for checker in self.get_checkers())

    async def run(self) -> tuple[str, httpx.URL | None] | None:
        found = await self.check()
        if not found:
            return None
        return (self.name, self.response_url)

    def get_url(self) -> str:
        return self.url.format(value=self.get_value())

    def get_headers(self) -> dict[str, Any]:
        return {"User-Agent": DEFAULT_USER_AGENT}

    def get_value(self) -> str:
        return self.value.strip().replace(" ", "-")

    def get_checkers(self) -> list[Checker]:
        if not self.checkers:
            return [StatusCodeChecker(code=200)]
        return self.checkers
