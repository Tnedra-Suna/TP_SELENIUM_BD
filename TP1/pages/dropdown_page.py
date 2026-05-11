# ### Partie 2 — Liste déroulante

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 1. Ouvrir la page Dropdown.
    def open(self):
        """Ouvrir la page Dropdown"""
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(self.DROPDOWN))

    # 2. Vérifier que la liste déroulante est présente.
    def is_dropdown_present(self):
        """Vérifier que la liste déroulante est présente"""
        try:
            return self.driver.find_element(*self.DROPDOWN).is_displayed()
        except Exception:
            return False

    #Retourne la sélection de l'élément
    def get_select(self):
        """Retourne la sélection de l'élément"""
        return Select(self.driver.find_element(*self.DROPDOWN))

    # 3. Sélectionner l'option
    def select_option_by_text(self, text):
        """Sélectionne l'option avec du text"""
        self.get_select().select_by_visible_text(text)
        
    # 4. Vérifier que `Option 1` est bien sélectionnée.
    def get_selected_option_text(self):
        """Récupère le texte de l'option séléctionnée"""
        return self.get_select().first_selected_option.text
