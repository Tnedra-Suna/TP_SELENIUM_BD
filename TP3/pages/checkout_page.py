from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Page Object saisie infos"""

    # Locators — Formulaire étape 1 (pas de dico ici je trouve ça plus clair)
    FIRSTNAME_INPUT = (By.ID, "first-name")
    LASTNAME_INPUT  = (By.ID, "last-name")
    POSTAL_INPUT    = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Locators — Récapitulatif étape 2
    SUMMARY_ITEMS   = (By.CLASS_NAME, "cart_item")
    ITEM_NAME       = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE      = (By.CLASS_NAME, "inventory_item_price")
    SUBTOTAL_LABEL  = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL       = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL     = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON   = (By.ID, "finish")

    def fill_customer_info(self, firstname: str, lastname: str, postal: str):
        self.logger.info(f"Saisie infos client : {firstname} {lastname}, {postal}")
        self.type_text(self.FIRSTNAME_INPUT, firstname)
        self.type_text(self.LASTNAME_INPUT, lastname)
        self.type_text(self.POSTAL_INPUT, postal)
        self.click(self.CONTINUE_BUTTON)

    def get_item_names(self) -> list:
        items = self.driver.find_elements(*self.ITEM_NAME)
        return [item.text for item in items]

    def get_item_price(self) -> str:
        return self.get_text(self.ITEM_PRICE)

    def get_subtotal(self) -> str:
        return self.get_text(self.SUBTOTAL_LABEL)

    def get_tax(self) -> str:
        return self.get_text(self.TAX_LABEL)

    def get_total(self) -> str:
        return self.get_text(self.TOTAL_LABEL)

    def finish_order(self):
        self.logger.info("Validation de la commande")
        self.click(self.FINISH_BUTTON)
        