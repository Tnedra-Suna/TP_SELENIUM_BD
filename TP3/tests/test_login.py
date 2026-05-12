import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger("test_login")

class TestLogin:
    """Scénarios 1 et 2 : Connexion réussie et refusée."""

    VALID_ID = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    INVALID_ID = "locked_out_user"
    
    def test_successful_login(self, driver):
        """Scénario 1 — Connexion réussie : standard_user"""
        
        logger.info("--- TEST si connexion réussie ---")

        login_page = LoginPage(driver)
        
        login_page.open().login(self.VALID_ID, self.VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        
        # * l’utilisateur accède à la page catalogue ;
        # * le titre de la page inventaire est visible.
        title = inventory_page.get_title()

        logger.info(f"Titre de la page : {title}")
        assert title == "Products", (f"Titre attendu : 'Products', titre obtenu : '{title}'")
        
        logger.info("Scénario 1 OK : Connexion réussie — page inventaire atteinte")

    def test_locked_out_user_login(self, driver):
        """Scénario 2 — Connexion refusée : locked_out_user."""
        
        logger.info("--- TEST si connexion refusée ---")

        login_page = LoginPage(driver)
        login_page.open().login(self.INVALID_ID, self.VALID_PASSWORD)

        # * un message d’erreur est affiché ;
        assert login_page.is_error_displayed(), ("Le message d'erreur devrait être affiché")

        error_msg = login_page.get_error_message()
        logger.info(f"Message d'erreur : {error_msg}")
        assert "locked out" in error_msg.lower(), (f"Le message ne mentionne pas 'locked out' : '{error_msg}'")

        # * l’utilisateur reste sur la page de connexion.
        assert "saucedemo.com" in driver.current_url and "inventory" not in driver.current_url, ("L'utilisateur ne devrait pas avoir accès au catalogue")
        
        logger.info("Scénario 2 OK : Connexion refusée — message d'erreur affiché")