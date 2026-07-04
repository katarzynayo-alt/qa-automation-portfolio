"""Базовый класс для всех Page Object'ов."""


class BasePage:
    """Содержит общие методы, которые нужны на всех страницах."""

    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
