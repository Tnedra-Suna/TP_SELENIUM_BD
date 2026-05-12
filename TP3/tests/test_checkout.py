# ## Scénario 4 — Parcours d’achat complet

# Automatiser le parcours suivant :

# 1. connexion ;
# 2. ajout du produit `Sauce Labs Backpack` ;
# 3. ouverture du panier ;
# 4. vérification du produit présent dans le panier ;
# 5. démarrage du checkout ;
# 6. saisie des informations client ;
# 7. vérification du récapitulatif ;
# 8. validation de la commande.

# Informations client à utiliser :

# ```text
# Prénom : John
# Nom : Doe
# Code postal : 59000
# ```

# Résultats attendus :

# * le récapitulatif contient bien `Sauce Labs Backpack` ;
# * le prix du produit est correct ;
# * le total hors taxe correspond au prix du produit ;
# * la taxe est affichée ;
# * le total final est cohérent ;
# * le message suivant est affiché après validation :

# ```text
# Thank you for your order!
# ```

# Screenshot demandé :

# * effectuer une capture d’écran de la page de confirmation finale.

# ---

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.logger import get_logger
from utils.screenshot import take_screenshot

logger = get_logger("test_checkout")

PRODUCT = "Sauce Labs Backpack"


class TestCheckout:
    """Scénario 4 — Parcours d'achat complet"""

    def test_complete_purchase(self, driver):
        """Effectue un achat E2E"""
        logger.info("--- TEST : Parcours d'achat complet ---")

        # 1. Connexion
        logger.info("Étape 1 : Connexion")
        LoginPage(driver).open().login("standard_user", "secret_sauce")

        # 2. Ajout du produit
        logger.info("Étape 2 : Ajout du produit au panier")
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart(PRODUCT)

        # 3. Ouverture du panier
        logger.info("Étape 3 : Ouverture du panier")
        inventory_page.open_cart()

        # 4. Vérification du produit dans le panier
        logger.info("Étape 4 : Vérification du panier")
        cart_page = CartPage(driver)
        item_names = cart_page.get_item_names()
        assert PRODUCT in item_names, (
            f"'{PRODUCT}' absent du panier. Contenu : {item_names}"
        )
        cart_price = cart_page.get_item_price()

        # 5. Démarrage du checkout
        logger.info("Étape 5 : Démarrage du checkout")
        cart_page.proceed_to_checkout()

        # 6. Saisie des informations client
        logger.info("Étape 6 : Saisie des informations client")
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_customer_info("John", "Doe", "59000")

        # 7. Vérification du récapitulatif
        logger.info("Étape 7 : Vérification du récapitulatif")
        summary_items = checkout_page.get_item_names()
        assert PRODUCT in summary_items, (f"'{PRODUCT}' absent du récapitulatif. Contenu : {summary_items}")

        item_price = checkout_page.get_item_price()
        assert item_price == cart_price, (f"Prix incohérent — panier : {cart_price}, récap : {item_price}")

        subtotal = checkout_page.get_subtotal()
        tax      = checkout_page.get_tax()
        total    = checkout_page.get_total()

        logger.info(f"Sous-total : {subtotal}")
        logger.info(f"Taxe : {tax}")
        logger.info(f"Total : {total}")

        assert "Item total:" in subtotal, "Le sous-total devrait être affiché"
        assert "Tax:" in tax, "La taxe devrait être affichée"
        assert "Total:" in total, "Le total devrait être affiché"

        # Cohérence : subtotal + tax = total
        def extract_price(label: str) -> float:
            return float(label.split("$")[-1].strip())

        subtotal_val = extract_price(subtotal)
        tax_val      = extract_price(tax)
        total_val    = extract_price(total)

        assert abs((subtotal_val + tax_val) - total_val) < 0.01, (f"Total incohérent : {subtotal_val} + {tax_val} ≠ {total_val}")

        # 8. Validation de la commande
        logger.info("Étape 8 : Validation finale")
        checkout_page.finish_order()

        complete_page = CheckoutCompletePage(driver)
        take_screenshot(driver, "checkout_complete_confirmation")
        logger.info("Screenshot de la page de confirmation pris")

        confirmation = complete_page.get_confirmation_header()
        assert complete_page.is_order_confirmed(), (f"Message de confirmation attendu, obtenu : '{confirmation}'")
        
        logger.info(f"Commande validée — Message : '{confirmation}'")