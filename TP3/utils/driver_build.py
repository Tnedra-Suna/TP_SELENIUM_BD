from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(headless: bool = True) -> webdriver.Chrome:
    """Fabrique le driver"""
    
    options = Options()
    
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")

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
    
    # Pour utiliser que des attentes explicites, on force les attentes implicites à 0
    driver.implicitly_wait(0)  
    return driver
