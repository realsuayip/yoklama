from yoklama.base import Module
from yoklama.checkers import HTMLContentsChecker, StatusCodeChecker


class InciSozluk(Module):
    name = "incisozluk.com.tr"
    url = "http://www.incisozluk.com.tr/u/{value}/"
    checkers = [
        StatusCodeChecker(code=200),
        HTMLContentsChecker("div", class_="userpage_nav"),
    ]
