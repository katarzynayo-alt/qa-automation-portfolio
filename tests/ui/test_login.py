"""UI-тесты логина на saucedemo.com."""

import pytest
from pages.login_page import LoginPage

pytestmark = pytest.mark.ui


def test_successful_login(page, credentials):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(credentials["username"], credentials["password"])

    assert "inventory.html" in page.url


def test_login_with_invalid_password(page, credentials):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(credentials["username"], "wrong_password")

    error_text = login_page.get_error_text()
    assert "Username and password do not match" in error_text


def test_login_with_empty_fields(page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login("", "")

    error_text = login_page.get_error_text()
    assert "Username is required" in error_text
