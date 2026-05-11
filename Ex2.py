# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://example.com
# 3. Trouvez le premier lien (tag "a") de la page
# 4. Vérifiez que c'est un lien (tag "a")
# 5. Vérifiez que le href est valide (non vide)
# 6. Affichez l'URL du lien
# 7. Fermez le navigateur

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    print("\n1. Navigation vers example.com...")
    driver.get("https://example.com")

    # 3. Trouvez le premier lien (tag "a") de la page
    # By.TAG_NAME permet de rechercher un élément par nom de balise HTML.
    element = driver.find_element(By.CSS_SELECTOR, "a") #Récupère un webelement
    print(f"3. Élément trouvé : {element.text}")
    
    # 4. Vérifiez que c'est un lien (tag "a")    
    # get_attribute(...) permet de lire la valeur d'un attribut HTML.
    tag_name = element.tag_name
    assert tag_name == "a", f"L'élément n'est pas un lien, tag trouvé : {tag_name}"
    print(f"4. Type d'élément vérifié : <{tag_name}>")
    
    # 5. Vérifiez que le href est valide (non vide)
    # get_attribute(...) permet de lire la valeur d'un attribut HTML.
    href = element.get_attribute("href")
    assert href is not None and len(href) > 0, f"URL invalide : {href}"
    # 6. Affichez l'URL du lien
    print(f"5. Le href est valide et contient : {href}")

    #Affiche l'URL actuelle
    print(f"URL actuelle : {driver.current_url}")
    
    
except AssertionError as e:
    print(f"Erreur d'assertion : {e}")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("\n6. Fermeture...")
    driver.quit()
    print("    Fermé")