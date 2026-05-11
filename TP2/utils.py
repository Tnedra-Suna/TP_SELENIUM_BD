import os, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

#Affichage message
def log(msg: str):
    #print(msg)
    logger.info(msg)


#À l’exécution, le script doit afficher clairement si les vérifications sont réussies ou non (permet d'afficher un message si c'est ok, un message si c'est pas ok)
def assert_true(condition: bool, ok_msg: str, fail_msg: str):
    """Fonction résultat assertion : succès ou échec"""
    if condition:
        print(f"REUSSI : {ok_msg}")
    else:
        raise AssertionError(f"ECHEC : {fail_msg}")

# * une capture d’écran en cas d’erreur ;
def screenshot_on_error(driver, test_name: str):
    """Une capture d’écran en cas d’erreur"""
    os.makedirs("screenshots", exist_ok=True)    
    screenshot_name = f"screenshots/{test_name.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(screenshot_name)
    print(f" Screenshot sauvegardé: {screenshot_name}")

#Gère les options du navigateur
def build_driver() -> webdriver.Chrome:
    options = Options()
    #options.add_argument("--headless=new")
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
        
    return webdriver.Chrome(options=options)