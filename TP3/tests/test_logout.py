


import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import get_logger

logger = get_logger("test_logout")


class TestLogout:
    """Scénario 5 — Déconnexion."""

    def test_logout(self, driver):
        """Vérifie que l'utilisateur est redirigé vers la page de login."""
        logger.info("--- TEST : Déconnexion ---")

        LoginPage(driver).open().login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.logout()

        current_url = driver.current_url
        logger.info(f"URL après déconnexion : {current_url}")

        assert "saucedemo.com" in current_url and "inventory" not in current_url, (
            f"L'utilisateur devrait être sur la page de login. URL actuelle : {current_url}"
        )

        login_page = LoginPage(driver)
        assert login_page.is_visible(LoginPage.LOGIN_BUTTON), (
            "Le bouton de connexion devrait être visible après déconnexion"
        )
        logger.info("Déconnexion réussie — retour sur la page de login")