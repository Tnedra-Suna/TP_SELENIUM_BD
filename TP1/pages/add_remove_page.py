# ### Partie 3 — Ajout et suppression d’éléments

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddRemovePage:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    ADD_BUTTON     = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTONS = (By.XPATH, "//button[text()='Delete']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 1. Ouvrir la page Add/Remove Elements.
    def open(self):
        """Ouvrir la page Add/Remove Elements"""
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located(self.ADD_BUTTON))

    # 2. Cliquer 3 fois sur `Add Element`.
    def click_add_element(self):
        """Cliquer sur `Add Element`"""
        self.driver.find_element(*self.ADD_BUTTON).click()

    # 3. Vérifier que 3 boutons `Delete` sont affichés.
    # 5. Vérifier qu’il reste 2 boutons `Delete`.
    # 7. Vérifier qu’il ne reste plus aucun bouton `Delete`.
    def get_delete_button_count(self):
        """Compteur de boutons 'Delete'"""
        return len(self.driver.find_elements(*self.DELETE_BUTTONS))

    # 4. Supprimer 1 élément.
    def click_first_delete_button(self):
        """Clique sur le premier 'Delete'"""
        buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
        if buttons:
            buttons[0].click()

    # 6. Supprimer tous les éléments restants.
    def delete_all_elements(self):
        """Supprime chaque bouton 'Delete'"""
        for btn in self.driver.find_elements(*self.DELETE_BUTTONS):
            btn.click()