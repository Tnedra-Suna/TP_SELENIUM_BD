# **Compétences**: Utiliser les sélecteurs CSS

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://practicesoftwaretesting.com/
# 3. Attendez que les produits se chargent
# 4. Localisez les cartes produit en utilisant le sélecteur CSS `a.card`
# 5. Localisez les titres de produits en utilisant le sélecteur CSS `.card-title`
# 6. Vérifiez que tous les éléments sont visibles
# 7. Comptez le nombre total de cartes produit
# 8. Fermez le navigateur

# **Validation**:
# - Tous les sélecteurs CSS fonctionnent
# - Les éléments sont trouvés
# - Le comptage est correct

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def exercicss6():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        # 2. Accédez à https://practicesoftwaretesting.com/
        driver.get("https://practicesoftwaretesting.com/")
        
        # 3. Attendez que les produits se chargent
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card")))
    
        # 4. Localisez les cartes produit en utilisant le sélecteur CSS `a.card`
        # ".card" sélectionne tous les éléments ayant la classe "card".
        product_cards = driver.find_elements(By.CSS_SELECTOR, "a.card")
        assert len(product_cards) == 9, f"Nombre de cartes incorrect : {len(product_cards)}"
        
        # 5. Localisez les titres de produits en utilisant le sélecteur CSS `.card-title`
        # ".card-title" sélectionne tous les éléments ayant cette classe.
        product_titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        assert len(product_titles) == 9, f"Nombre de titres incorrect : {len(product_titles)}"
        
        # 6. Vérifiez que tous les éléments sont visibles
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card"))
        
        #Solution 2 ? : is_displayed() indique si l'élément est visible à l'écran.
        visible_elements = [card for card in product_cards if card.is_displayed()]
        assert len(visible_elements) == 9, f"Nombre de cards visibles incorrect : {len(visible_elements)}"
        
        # 7. Comptez le nombre total de cartes produit
        print(f"Le nombre de cards est : {len(product_cards)}")

        print("Exo 6 OK")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("\n6. Fermeture...")
        driver.quit()
        print("    Fermé")


if __name__ == "__main__":
    exercicss6()