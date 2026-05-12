from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    """Page Object confirmation de commande"""

    # Locators
    CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")
    CONFIRMATION_TEXT   = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BUTTON    = (By.ID, "back-to-products")

    def get_confirmation_header(self) -> str:
        return self.get_text(self.CONFIRMATION_HEADER)

    def get_confirmation_text(self) -> str:
        return self.get_text(self.CONFIRMATION_TEXT)

    def is_order_confirmed(self) -> bool:
        return "Thank you for your order!" in self.get_confirmation_header()