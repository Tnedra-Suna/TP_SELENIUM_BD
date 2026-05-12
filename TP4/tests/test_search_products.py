"""
Test automatisé — TP4 Selenium Python
Site : https://automationexercise.com/
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from utils.logger_config import setup_logger
from utils.screenshot import take_screenshot
from utils.report import generate_report

SEARCH_KEYWORD = "top"

def run_test():
    logger = setup_logger()
    logger.info("═" * 60)
    logger.info("  Démarrage du test TP4")
    logger.info("═" * 60)

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--window-size=1920,1080")
    
    # Préférences internes de Chrome
    # Elles permettent notamment d'éviter des alertes liées aux mots de passe
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    # Ajoute les préférences Chrome à la configuration du navigateur
    options.add_experimental_option("prefs", prefs)
        
    driver = webdriver.Chrome(options=options)

    success = True
    errors = []
    products = []

    try:
        # Étape 1 : Ouvrir le site 
        logger.info("Étape 1 — Ouverture du site")
        home = HomePage(driver)
        home.open()
        logger.info("Site ouvert : %s", driver.current_url)

        screenshot_home = take_screenshot(driver, "01_home")
        logger.info("Screenshot enregistré : %s", screenshot_home)

        # Étape 2 : Accéder à la page Products
        logger.info("Étape 2 — Navigation vers la page Products")
        home.go_to_products()

        products_page = ProductsPage(driver)
        products_page.wait_for_load()
        logger.info("Page Products chargée")

        # Étape 3 : Rechercher un mot-clé 
        logger.info("Étape 3 — Recherche du mot-clé : '%s'", SEARCH_KEYWORD)
        products_page.search(SEARCH_KEYWORD)
        logger.info("Recherche effectuée")

        # Étape 4 : Récupérer les produits
        logger.info("Étape 4 — Récupération des produits")
        products = products_page.get_products()
        logger.info("Nombre de produits trouvés : %d", len(products))

        screenshot_results = take_screenshot(driver, "02_search_results")
        logger.info("Screenshot enregistré : %s", screenshot_results)

        # Étape 5 : Assertions
        logger.info("Étape 5 — Vérification des assertions")

        # Assertion 1 — au moins un produit affiché
        assert len(products) > 0, \
            f"Assertion 1 échouée : aucun produit trouvé pour '{SEARCH_KEYWORD}'"
        logger.info(" Assertion 1 OK — %d produit(s) trouvé(s)", len(products))

        # Assertion 2 — tous les noms contiennent "top" (insensible à la casse)
        failing = [p for p in products if SEARCH_KEYWORD.lower() not in p.name.lower()]
        assert len(failing) == 0, (
            f"Assertion 2 échouée — produits sans '{SEARCH_KEYWORD}' : "
            + ", ".join(p.name for p in failing)
        )
        logger.info("Assertion 2 OK — tous les noms contiennent '%s'", SEARCH_KEYWORD)

        # Assertion 3 — titre contient "Automation Exercise"
        page_title = driver.title
        assert "Automation Exercise" in page_title, \
            f"Assertion 3 échouée — titre inattendu : '{page_title}'"
        logger.info("Assertion 3 OK — titre : '%s'", page_title)

    except AssertionError as e:
        success = False
        error_msg = str(e)
        errors.append(error_msg)
        logger.error("Assertion échouée : %s", error_msg)
        take_screenshot(driver, "03_error")

    except Exception as e:
        success = False
        error_msg = f"Erreur inattendue : {e}"
        errors.append(error_msg)
        logger.exception("Erreur inattendue : %s", e)
        take_screenshot(driver, "03_error")

    finally:
        driver.quit()
        logger.info("Navigateur fermé")

        report = generate_report(products, success, errors)
        print("\n" + report)
        logger.info("Fin du test — succès : %s", success)

    return success


if __name__ == "__main__":
    run_test()