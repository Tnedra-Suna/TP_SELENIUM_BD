from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from pages.product_card import ProductCard


class ProductsPage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    SEARCH_INPUT  = (By.CSS_SELECTOR, "input#search_product")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button#submit_search")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".features_items .col-sm-4")
    PRODUCT_NAME  = (By.CSS_SELECTOR, "p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h2")
    OVERLAY       = (By.CSS_SELECTOR, "div.fc-dialog-overlay")

    #Méthode privée
    def _close_overlay(self):
        """Supprime la popup consent/pub si elle est présente."""
        try:
            self.wait.until(EC.visibility_of_element_located(self.OVERLAY))
            self.driver.execute_script("document.querySelectorAll('.fc-dialog-overlay, .fc-dialog-container')" ".forEach(el => el.remove());")
            self.wait.until(EC.invisibility_of_element_located(self.OVERLAY))
        except Exception:
            pass

    def _js_click(self, locator):
        """Attend qu'un élément soit présent et clique dessus via JS."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)


    
    def wait_for_load(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        self._close_overlay()

    def search(self, keyword: str):
        self._close_overlay()
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_box.clear()
        search_box.send_keys(keyword)
        self._js_click(self.SEARCH_BUTTON)   # ← clic JS, immunisé contre les overlays
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_ITEMS))

    def get_products(self) -> list[ProductCard]:
        items = self.driver.find_elements(*self.PRODUCT_ITEMS)
        products = []
        for item in items:
            try:
                name  = item.find_element(*self.PRODUCT_NAME).text.strip()
                price = item.find_element(*self.PRODUCT_PRICE).text.strip()
                if name:
                    products.append(ProductCard(name=name, price=price))
            except Exception:
                continue
        return products