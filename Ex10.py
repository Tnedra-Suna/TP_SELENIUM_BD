# **Compétences**: Boucler sur les éléments, extraire du texte

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://practicesoftwaretesting.com/
# 3. Attendez que les produits se chargent 
# 4. Localisez tous les éléments produit
# 5. Pour chaque produit, extrayez:
#    - Le nom du produit 
#    - Le prix (et si en rupture de stock)
# 6. Créez une liste Python avec tous les produits
# 7. Affichez les 5 premiers produits
# 8. Affichez la liste complète
# 9. Fermez le navigateur

# **Validation**:
# - Tous les produits sont trouvés
# - Les données sont extraites correctement
# - La liste Python est créée et affichée

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def exercice10():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 2. Accédez à https://practicesoftwaretesting.com/
        driver.get("https://practicesoftwaretesting.com/")
        
        # 3. Attendez que les produits se chargent 
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.card")))

        # 4. Localisez tous les éléments produit
        produit_elements = driver.find_elements(By.CSS_SELECTOR, "a.card")
        
        # 5. Pour chaque produit, extrayez:
        #    - Le nom du produit 
        #    - Le prix (et si en rupture de stock)
        produits = []
        
        for produit in produit_elements:
            #    - Le nom du produit 
            nom = produit.find_element(By.CSS_SELECTOR, ".card-title").text.strip()

            #    - Le prix (et si en rupture de stock)
            try:
                prix_element = produit.find_element(By.CSS_SELECTOR, "[data-test='product-price']")
                prix_text = prix_element.text.strip()

                # Si rupture de stock
                if "Rupture de stock" in prix_text:
                    prix = "Rupture de stock"
                else:
                    prix = prix_text
            except:
                prix = "Rupture de stock"
                
            # 6. Créez une liste Python avec tous les produits
            produits.append({"nom": nom, "prix": prix})
        
        # 7. Affichez les 5 premiers produits
        print("\nLes 5 premiers produits sont : ")
        for i, n in enumerate(produits[:5], 1):
            print(f"{i}. {n['nom']} = {n['prix']}")
        
        # 8. Affichez la liste complète
        print("\nLa liste complète est : ")
        for i, n in enumerate(produits, 1):
            print(f"{i}. {n['nom']} = {n['prix']}")
    
        #Bonus : enregistrer les produits dans un fichier json 
        
        print("Exercice 10 OK")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("\n6. Fermeture...")
        driver.quit()
        print("    Fermé")


if __name__ == "__main__":
    exercice10()