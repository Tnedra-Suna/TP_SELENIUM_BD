from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    URL = "https://practicesoftwaretesting.com"
    
    CARDS = (By.CSS_SELECTOR, "a.card")
    RESULT_PAGE = (By.CSS_SELECTOR, "[data-test='search_completed']")
    SEARCH_RESULT = (By.CSS_SELECTOR, "[data-test='product-name']")
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
    
    def wait_for_all_elements(self):
        self.wait.until(EC.presence_of_all_elements_located(self.CARDS))
 
    #    - Vérifiez que vous êtes sur la page de résultats
    def wait_for_research_page(self):
        self.wait.until(EC.visibility_of_element_located(self.RESULT_PAGE))
    
    #    - Vérifiez qu'au moins un résultat est affiché
    def wait_for_one_element_visible(self):
        self.search_result = self.driver.find_elements(*self.SEARCH_RESULT)
        assert len(self.search_result) >= 1, "Aucun résultat affiché !"
        return self.search_result
    
    #Manque tâche 3