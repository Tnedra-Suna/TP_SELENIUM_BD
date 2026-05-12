from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object pour la page de connexion."""

    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME_INPUT  = (By.ID, "user-name")
    PASSWORD_INPUT  = (By.ID, "password")
    LOGIN_BUTTON    = (By.ID, "login-button")
    ERROR_MESSAGE   = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.logger.info(f"Ouverture de {self.URL}")
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str):
        self.logger.info(f"Connexion avec l'utilisateur : {username}")
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)