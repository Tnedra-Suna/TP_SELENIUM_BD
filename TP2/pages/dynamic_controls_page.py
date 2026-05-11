### Partie 1 — Dynamic Controls

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    CHECKBOX       = (By.ID, "checkbox")
    BTN_REMOVE_ADD = (By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
    RESULT_MSG     = (By.ID, "message")
    TEXT_INPUT     = (By.CSS_SELECTOR, "#input-example input[type='text']")
    ENABLE_BTN     = (By.CSS_SELECTOR, "#input-example button")

    # 1. Ouvrir la page Dynamic Controls.
    # # 2. Vérifier que la page est bien chargée.
    def open(self):
        super().open(self.URL)
        self.wait_visible(self.BTN_REMOVE_ADD)

    # 3. Vérifier que la case à cocher est présente.
    def is_checkbox_present(self) -> bool:
        return len(self.find_all(self.CHECKBOX)) > 0

    # 4. Cliquer sur `Remove`.
    # 7. Cliquer sur `Add`.
    def click_remove_add(self):
        self.wait_clickable(self.BTN_REMOVE_ADD).click()

    # 5. Attendre correctement la disparition de la case à cocher.
    def wait_checkbox_removed(self):
        self.wait_invisible(self.CHECKBOX)

    # 8. Attendre correctement la réapparition de la case à cocher.
    def wait_checkbox_added(self):
        self.wait_visible(self.CHECKBOX)

    # 6. Vérifier le message de confirmation affiché.
    # 9. Vérifier le nouveau message de confirmation.
    def get_result_message(self) -> str:
        return self.wait_visible(self.RESULT_MSG).text.strip()



    # 10. Dans la zone `Enable/disable`, vérifier que le champ texte est initialement désactivé.
    def is_input_disabled(self) -> bool:
        return not self.find(self.TEXT_INPUT).is_enabled()

    # 11. Cliquer sur `Enable`.
    def click_enable_disable(self):
        self.wait_clickable(self.ENABLE_BTN).click()

    # 12. Attendre correctement que le champ devienne actif.
    def wait_input_enabled(self):
        self.wait.until(EC.element_to_be_clickable(self.TEXT_INPUT))

    # 13. Vérifier qu’il est maintenant possible d’écrire dedans.
    def type_in_input(self, text: str):
        field = self.find(self.TEXT_INPUT)
        field.clear()
        field.send_keys(text)

    # 14. Saisir un texte de test et vérifier qu’il a bien été saisi.
    def get_input_value(self) -> str:
        return self.find(self.TEXT_INPUT).get_attribute("value")