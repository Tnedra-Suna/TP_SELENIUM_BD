
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object pour la page panier."""

    # Locators
    PAGE_TITLE      = (By.CLASS_NAME, "title")
    CART_ITEMS      = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_NAME       = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE      = (By.CLASS_NAME, "inventory_item_price")

    def get_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_item_names(self) -> list:
        items = self.driver.find_elements(*self.ITEM_NAME)
        return [item.text for item in items]

    def get_item_price(self) -> str:
        return self.get_text(self.ITEM_PRICE)

    def proceed_to_checkout(self):
        self.logger.info("Clic sur Checkout")
        self.click(self.CHECKOUT_BUTTON)