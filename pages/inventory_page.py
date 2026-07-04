"""Page Object для страницы со списком товаров (после логина)."""

from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    INVENTORY_ITEM = ".inventory_item"

    def add_item_to_cart_by_name(self, item_name: str):
        # Преобразуем имя товара в id кнопки, как это сделано на сайте
        button_id = "add-to-cart-" + item_name.lower().replace(" ", "-")
        self.page.click(f"#{button_id}")

    def get_cart_count(self) -> str:
        return self.page.text_content(self.CART_BADGE)

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def get_items_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEM).count()
