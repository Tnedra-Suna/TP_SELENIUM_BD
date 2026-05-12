# ## Scénario 3 — Ajout d’un produit au panier

# Après connexion avec `standard_user`, ajouter le produit suivant :

# ```text
# Sauce Labs Backpack
# ```

# Résultats attendus :

# * le bouton du produit passe de `Add to cart` à `Remove` ;
# * l’icône du panier affiche `1` ;
# * le panier contient bien `Sauce Labs Backpack` ;
# * le prix affiché dans le panier correspond au prix du produit sélectionné.

# Screenshot demandé :

# * effectuer une capture d’écran après l’ajout du produit au panier.

# ---

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger("test_cart")

PRODUCT = "Sauce Labs Backpack"


class TestCart:
    """Scénario 3 — Ajout d'un produit au panier."""

    def test_add_product_to_cart(self, driver):
        """Vérifie l'ajout du Sauce Labs Backpack au panier"""
        
        logger.info("--- TEST : Ajout produit au panier ---")

        # Connexion
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        inventory_page = InventoryPage(driver)

        # Ajout au panier
        inventory_page.add_product_to_cart(PRODUCT)
        logger.info(f"Produit ajouté : {PRODUCT}")
        
        # Vérification : bouton passe à "Remove"
        remove_btn_text = inventory_page.get_remove_button_text(PRODUCT)
        assert remove_btn_text.lower() == "remove", (f"Le bouton devrait afficher 'Remove', obtenu : '{remove_btn_text}'")

        # Vérification panier = 1
        cart_count = inventory_page.get_cart_count()
        assert cart_count == 1, f"Le panier devrait contenir 1 article : {cart_count}"

        # Screenshot après ajout au panier
        take_screenshot(driver, "add_to_cart_backpack")
        logger.info("Screenshot pris après ajout au panier")

        # Vérification produit est bien dans le panier
        inventory_page.open_cart()
        cart_page = CartPage(driver)
        item_names = cart_page.get_item_names()
        assert PRODUCT in item_names, (f"'{PRODUCT}' devrait être dans le panier. Contenu : {item_names}")

        item_price = cart_page.get_item_price()
        logger.info(f"Prix du produit dans le panier : {item_price}")
        assert "$" in item_price, "Le prix devrait contenir le symbole '$'"

        logger.info("Produit ajouté et OK dans le panier")
        
        #Vide le panier sinon le scénario 4 ne fonctionnera pas
        inventory_page.remove_product_cart(PRODUCT)
        logger.info(f"Produit retiré : {PRODUCT}")
        

        