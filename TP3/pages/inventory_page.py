from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object inventaire)."""

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def add_product_to_cart(self, product_name: str):
        """Ajoute un produit au panier avec bouton par data-test"""
        safe_name = product_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{safe_name}']")
        self.logger.info(f"Ajout au panier : {product_name}")
        self.click(locator)
        
    def remove_product_cart(self, product_name: str):
        """Retire un produit du panier avec bouton par data-test"""
        safe_name = product_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR, f"[data-test='remove-{safe_name}']")
        self.logger.info(f"Enelevé du panier : {product_name}")
        self.click(locator)


    def get_add_button_text(self, product_name: str) -> str:
        safe_name = product_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR,
            f"[data-test='add-to-cart-{safe_name}'], [data-test='remove-{safe_name}']")
        return self.find_visible(locator).text

    def get_remove_button_text(self, product_name: str) -> str:
        safe_name = product_name.lower().replace(" ", "-")
        locator = (By.CSS_SELECTOR, f"[data-test='remove-{safe_name}']")
        return self.find_visible(locator).text

    def get_cart_count(self) -> int:
        try:
            return int(self.get_text(self.CART_BADGE))
        except Exception:
            return 0

    def open_cart(self):
        self.logger.info("Ouverture du panier")
        self.click(self.CART_LINK)

    def logout(self):
        self.logger.info("Déconnexion via le menu")
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)