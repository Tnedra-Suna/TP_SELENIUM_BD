# **Compétences**: Utiliser les XPath

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://practicesoftwaretesting.com/
# 3. Attendez que les produits se chargent
# 4. Localisez les cartes produit en utilisant XPath avec `contains()` pour la classe
# 5. Localisez les titres de produits en utilisant XPath (Testez différentes variations de XPath: position, not(), descendant)
# 6. Vérifiez que tous les éléments sont trouvés
# 7. Fermez le navigateur

# **Validation**:
# - Tous les XPath fonctionnent
# - Les éléments sont correctement localisés
# - Les variantes de XPath fonctionnent

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def exercice7():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # 2. Accédez à https://practicesoftwaretesting.com/
        driver.get("https://practicesoftwaretesting.com/")
        
        # 3. Attendez que les produits se chargent
        # visibility_of_element_located attend qu'un élément existe et soit visible.
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card")))
        
        # 4. Localisez les cartes produit en utilisant XPath avec `contains()` pour la classe
        # contains(@class, 'card') est pratique quand un élément peut avoir plusieurs classes.
        cards = driver.find_elements(By.XPATH, "//a[contains(@class, 'card')]")
        assert len(cards) == 9, f"Nombre de cartes incorrect : {len(cards)}"

        # 5. Localisez les titres de produits en utilisant XPath (Testez différentes variations de XPath: position, not(), descendant)
        # contains(...) peut aussi servir à trouver des titres par classe partielle.
        #titles = driver.find_elements(By.XPATH, "//h5[contains(@datat-test, 'product-name')]")
        titles = driver.find_elements(By.XPATH, "//*[contains(@class, 'card-title')]")
        assert len(titles) == 9, f"Nombre de titres incorrect : {len(titles)}"
        assert titles[0].text == "Combination Pliers", f"Premier titre incorrect : {titles[0].text}"
        
        # 6. Vérifiez que tous les éléments sont trouvés
        #Plutôt avec un for
        for title in titles:
            print(title.text)
            
        # for i in range(min(3, len(titles))):
        #     title = driver.find_elements(By.CSS_SELECTOR, ".card-titles")[i]
        #     print(f" Produit {i+1}: {title.text}")
                  
        EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'card')]"))  
        
        print("Exo 7 OK")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("\n6. Fermeture...")
        driver.quit()
        print("    Fermé")


if __name__ == "__main__":
    exercice7()