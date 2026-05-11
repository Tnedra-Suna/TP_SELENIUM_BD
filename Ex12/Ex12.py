
# ## TP Recherche Basique et Extraction de Données
# **Site**: practicesoftwaretesting.com
# **Objectif**: Automatiser une recherche simple et extraire les résultats
# **Tâches**:

# 1. **Navigation et Localisation**
#    - Accédez à https://practicesoftwaretesting.com
#    - Localisez le formulaire de recherche principal
#    - Identifiez le champ texte de recherche
#    - Identifiez le bouton de recherche
#    - Vérifiez que ces éléments sont visibles

# 2. **Recherche de Produits**
#    - Saisissez "hammer" dans le champ de recherche
#    - Attendez explicitement la soumission
#    - Attendez que les résultats de recherche se chargent
#    - Vérifiez que vous êtes sur la page de résultats
#    - Vérifiez qu'au moins un résultat est affiché

# 3. **Extraction de Données**
#    - Localisez le conteneur des produits
#    - Pour chaque produit affiché:
#      - Extrayez le nom du produit
#      - Extrayez le prix du produit
#      - Extrayez la note (si disponible)
#    - Créez une liste Python contenant tous les produits avec leurs infos

# 4. **Validation et Rapport**
#    - Affichez le nombre total de résultats trouvés
#    - Affichez les 3 premiers produits avec leurs prix
#    - Affichez le produit le moins cher
#    - Affichez le produit le plus cher

# **Points de Contrôle**:
# - La recherche s'exécute correctement
# - Les résultats sont chargés
# - Les données sont extraites sans erreur
# - Le tri et l'affichage fonctionnent

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from home_page import HomePage
from search_result_page import ResultPage
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    home_page = HomePage(driver)
    result_page = ResultPage(driver)
    
# 1. **Navigation et Localisation**
    print("TÂCHE 1 — Navigation et Localisation")  
    
    #    - Accédez à https://practicesoftwaretesting.com
    home_page.open()
    
    #    - Localisez le formulaire de recherche principal
    #    - Identifiez le champ texte de recherche
    search_query = home_page.search_query()
     
    #    - Identifiez le bouton de recherche
    search_button = home_page.search_button()
    
    #    - Vérifiez que ces éléments sont visibles
    home_page.element_is_visible(search_query)
    home_page.element_is_visible(search_button) 
    
    
# 2. **Recherche de Produits** (possible de faire le lien avec une base_page pour les fonctions)
    print("\nTÂCHE 2 — Recherche de Produits")
    
    #    - Saisissez "hammer" dans le champ de recherche - Attendez explicitement la soumission
    print("Saisie de hammer")
    home_page.search_by_text(search_query, search_button, 'hammer')
 
    #    - Attendez que les résultats de recherche se chargent 
    result_page.wait_for_all_elements()
    print("Résultats complétement chargés")
    
    #    - Vérifiez que vous êtes sur la page de résultats
    result_page.wait_for_research_page()
    print("Nous sommes bien sur la page de résultats")
    
    #    - Vérifiez qu'au moins un résultat est affiché
    result = result_page.wait_for_one_element_visible()
    print(f"Nombre de résultats affichés : {len(result)}")





# 3. **Extraction de Données**
    print("\nTÂCHE 3 — Extraction de Données")
    
#    - Localisez le conteneur des produits
    product_cards = driver.find_elements(By.CSS_SELECTOR, "a.card")
    print(f"Cards produit trouvées : {len(product_cards)}")

#    - Pour chaque produit affiché: nom / prix / note (si disponible) - Créez une liste Python contenant tous les produits avec leurs infos
    produits = []
    for card in product_cards:
        nom = card.find_element(By.CSS_SELECTOR, "[data-test='product-name']").text.strip()

        prix_txt = card.find_element(By.CSS_SELECTOR, "[data-test='product-price']").text.strip()
        prix = float(prix_txt.replace("$", "").replace(",", ".").strip())
        
        # Note si dispo --> protection dans un try catch
        try:
            note_elem = card.find_element(By.CSS_SELECTOR, ".co2-letter.active")
            note = note_elem.text.strip()
        except Exception:
            note = "Pas de note"

        produit = {"nom": nom, "prix": prix, "prix_affiche": prix_txt, "note": note}
        produits.append(produit)
        print(f"{nom} | {prix_txt} | Note : {note}")

# 4. **Validation et Rapport**
    print("\nTÂCHE 4 — Validation et Rapport")

#    - Affichez le nombre total de résultats trouvés
    print(f"\nNombre total de résultats trouvés : {len(produits)}")
    
#    - Affichez les 3 premiers produits avec leurs prix
    print("\nLes 3 premiers produits :")
    for i, p in enumerate(produits[:3], start=1):
        print(f"  {i}. {p['nom']} à {p['prix_affiche']}")

#    - Affichez le produit le moins cher
    moins_cher = min(produits, key=lambda p: p["prix"])
    print(f"\nProduit le moins cher : {moins_cher['nom']} à {moins_cher['prix_affiche']}")

#    - Affichez le produit le plus cher
    plus_cher  = max(produits, key=lambda p: p["prix"])
    print(f"Produit le plus cher  : {plus_cher['nom']} à {plus_cher['prix_affiche']}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("\n6. Fermeture...")
    driver.quit()
    print("    Fermé")
    
    