"""Общие фикстуры для всех тестов."""

import pytest


# Данные для логина (валидный пользователь saucedemo)
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def credentials():
    return {"username": VALID_USER, "password": VALID_PASSWORD}
