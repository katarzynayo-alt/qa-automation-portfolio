"""UI-тесты добавления товара в корзину на saucedemo.com."""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

pytestmark = pytest.mark.ui


@pytest.fixture
def logged_in_page(page, credentials):
    """Логинит пользователя и возвращает page, готовую к работе с инвентарём."""
    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(credentials["username"], credentials["password"])
    return page


def test_add_single_item_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")

    assert inventory_page.get_cart_count() == "1"


def test_inventory_has_items(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    assert inventory_page.get_items_count() == 6
