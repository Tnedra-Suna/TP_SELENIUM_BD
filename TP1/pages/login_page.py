# ### Partie 1 — Authentification

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']")
    PAGE_HEADING   = (By.TAG_NAME, "h2")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 1. Ouvrir la page de login.
    def open(self):
        """Ouvre la page login et attend le bouton LOGIN"""
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))

    # 2. Vérifier que le titre ou le contenu de la page correspond bien à une page d’authentification.
    # 9. Vérifier que l’utilisateur revient bien sur la page de login.
    def get_heading_text(self):
        """Renvoie le text du heading"""
        return self.driver.find_element(*self.PAGE_HEADING).text

    # 3. Saisir le username fourni.
    def enter_username(self, username):
        """Entrer username"""
        field = self.driver.find_element(*self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)

    # 3. Saisir le password fourni.
    def enter_password(self, password):
        """Entrer password"""
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)

    # 4. Cliquer sur le bouton de connexion.
    def click_login(self):
        """Cliquer sur le bouton de connexion."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # Fonction qui fait les étapes de LOGIN
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()