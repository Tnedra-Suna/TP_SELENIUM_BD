from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://automationexercise.com/"


class HomePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    PRODUCTS_NAV    = (By.CSS_SELECTOR, "a[href='/products']")
    OVERLAY         = (By.CSS_SELECTOR, "div.fc-dialog-overlay")
    OVERLAY_CLOSE   = (By.CSS_SELECTOR, "button.fc-close, button.fc-cta-consent, "
                                         "button.fc-button.fc-cta-do-not-consent, "
                                         "[aria-label='Consent'], .fc-dialog button")

    # Méthode privée
    def _close_overlay(self):
        """Ferme la popup consent/pub si elle est présente."""
        try:
            # Attendre que l'overlay soit visible (max 6s)
            self.wait.until(EC.visibility_of_element_located(self.OVERLAY))

            # Tenter de cliquer sur un bouton de fermeture
            try:
                close_btn = self.driver.find_element(*self.OVERLAY_CLOSE)
                close_btn.click()
            except Exception:
                # Si aucun bouton trouvé, supprimer l'overlay via JS
                self.driver.execute_script(
                    "document.querySelectorAll('.fc-dialog-overlay, .fc-dialog-container')"
                    ".forEach(el => el.remove());"
                )

            # Attendre la disparition de l'overlay
            self.wait.until(EC.invisibility_of_element_located(self.OVERLAY))

        except Exception:
            # Pas d'overlay détecté, on continue normalement
            pass


    def open(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        self.wait.until(EC.presence_of_element_located(self.PRODUCTS_NAV))
        self._close_overlay()

    def go_to_products(self):
        self._close_overlay()  # sécurité si l'overlay réapparaît
        link = self.wait.until(EC.element_to_be_clickable(self.PRODUCTS_NAV))
        try:
            link.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", link)