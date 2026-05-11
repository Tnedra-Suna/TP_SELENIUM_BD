### Partie 2 — Dynamic Loading

# Automatiser le scénario suivant :

# 1. Ouvrir la page Dynamic Loading.
# 2. Aller sur `Example 2: Element rendered after the fact`.
# 3. Vérifier que le bouton `Start` est présent.
# 4. Cliquer sur `Start`.
# 5. Attendre correctement l’apparition du contenu chargé dynamiquement.
# 6. Vérifier que le texte `Hello World!` apparaît bien.

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DynamicLoadingPage(BasePage):
    URL_EXAMPLE_2 = "https://the-internet.herokuapp.com/dynamic_loading/2"

    START_BTN   = (By.CSS_SELECTOR, "#start button")
    LOADING_BAR = (By.ID, "loading")
    FINISH_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def open_example_2(self):
        super().open(self.URL_EXAMPLE_2)
        self.wait_visible(self.START_BTN)

    def is_start_button_present(self) -> bool:
        try:
            return self.find(self.START_BTN).is_displayed()
        except Exception:
            return False

    def click_start(self):
        self.wait_clickable(self.START_BTN).click()

    def wait_for_content(self) -> str:
        """Attend la disparition du loader puis retourne le texte chargé."""
        self.wait_invisible(self.LOADING_BAR)
        return self.wait_visible(self.FINISH_TEXT).text.strip()