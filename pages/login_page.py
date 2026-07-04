"""Page Object для страницы логина saucedemo.com."""

from pages.base_page import BasePage

URL = "https://www.saucedemo.com"


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def open_login_page(self):
        self.open(URL)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_text(self) -> str:
        return self.page.text_content(self.ERROR_MESSAGE)
