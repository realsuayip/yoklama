from slugify import slugify

from yoklama.base import Module
from yoklama.checkers import HTMLContentsChecker, StatusCodeChecker


class MemurlarSozluk(Module):
    name = "sozluk.memurlar.net"
    url = "https://sozluk.memurlar.net/yazar/{value}/"
    checkers = [
        StatusCodeChecker(code=200),
        HTMLContentsChecker("div", id="MemberTab"),
    ]

    def get_value(self) -> str:
        value = super().get_value()
        return slugify(value)
