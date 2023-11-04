from yoklama.base import Module
from yoklama.checkers import HTMLContentsChecker, StatusCodeChecker


class UludagSozluk(Module):
    name = "uludagsozluk.com"
    url = "https://www.uludagsozluk.com/{value}"
    checkers = [
        StatusCodeChecker(code=200),
        HTMLContentsChecker("div", class_="user-menu"),
    ]
