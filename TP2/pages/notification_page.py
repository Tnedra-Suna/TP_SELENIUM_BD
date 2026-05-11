### Partie 3 — Notification Message

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NotificationPage(BasePage):
    URL = "https://the-internet.herokuapp.com/notification_message_rendered"

    EXPECTED_MESSAGES = [
        "Action successful",
        "Action unsuccesful, please try again",
    ]

    CLICK_LINK = (By.LINK_TEXT, "Click here")
    NOTIFICATION = (By.ID, "flash")

    # 1. Ouvrir la page Notification Message.
    def open(self):
        super().open(self.URL)
        #self.wait_visible(self.NOTIFICATION)

    # 2. Lire le message affiché.
    def get_notification_text(self) -> str:
        raw = self.wait_visible(self.NOTIFICATION).text
        return raw.replace("×", "").strip()

    # 3. Cliquer sur `Click here` pour charger une nouvelle notification.
    def click_here(self):
        self.wait_clickable(self.CLICK_LINK).click()

    # 4. Vérifier qu’un message est bien affiché après le clic.
    def click_and_get_message(self) -> str:
        self.click_here()
        return self.get_notification_text()
    
    # 6. Vérifier que le message obtenu appartient bien aux messages attendus.
    def is_valid_message(self, text: str) -> bool:
        return any(expected in text for expected in self.EXPECTED_MESSAGES)