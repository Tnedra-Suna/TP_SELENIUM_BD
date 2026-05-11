from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    URL = "https://practicesoftwaretesting.com"
    
    SEARCH_QUERY = (By.ID, "search-query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def search_query(self):
        '''Identifiez la zone de recherche'''
        self.element_search_query = self.wait.until(EC.visibility_of_element_located(self.SEARCH_QUERY))
        return self.element_search_query
    
    def search_button(self):
        '''Identifiez le bouton de recherche'''
        self.element_search_button = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BUTTON))
        return self.element_search_button

    def element_is_visible(self, element):
        return element.is_displayed()
    
    def search_by_text(self, input, button, text):
        input.clear()
        input.send_keys(text)
        button.click()
        
        
    
    