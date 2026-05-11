# ### Partie 1 — Authentification

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SecureAreaPage:
    _SUCCESS_FLASH = (By.CSS_SELECTOR, "#flash.success")
    _LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")
    _PAGE_HEADING  = (By.TAG_NAME, "h2")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 5. Vérifier que la connexion a réussi.
    def get_heading_text(self):
        """Récupère le titre de la page"""
        return self.driver.find_element(*self._PAGE_HEADING).text

    # 6. Vérifier la présence du message de succès.
    def get_flash_message(self):
        """Récupère le message flash"""
        return self.wait.until(EC.visibility_of_element_located(self._SUCCESS_FLASH)).text

    # 7. Vérifier la présence du bouton ou lien de logout.
    def is_logout_button_present(self):
        """Regarde si le bouton logout est présent"""
        try:
            return self.driver.find_element(*self._LOGOUT_BUTTON).is_displayed()
        except Exception:
            return False

    # 8. Cliquer sur logout.
    def click_logout(self):
        self.driver.find_element(*self._LOGOUT_BUTTON).click()