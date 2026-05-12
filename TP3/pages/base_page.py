from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from utils.logger import get_logger
from utils.screenshot import take_screenshot

class BasePage:
    """Classe base pour tous les Page Objects"""

    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.TIMEOUT)
        self.logger = get_logger(self.__class__.__name__)

    def find(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        self.logger.debug(f"Click sur {locator}")
        self.find_clickable(locator).click()

    def type_text(self, locator: tuple, text: str):
        self.logger.debug(f"Saisie '{text}' dans {locator}")
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find_visible(locator).text

    def is_visible(self, locator: tuple) -> bool:
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).is_displayed()
        except Exception:
            return False

    def screenshot_on_error(self, test_name: str):
        take_screenshot(self.driver, f"ERROR_{test_name}")