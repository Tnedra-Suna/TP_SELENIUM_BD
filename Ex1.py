# **Instructions**:
# 1. Ouvrez un navigateur Chrome
# 2. Accédez à https://example.com
# 3. Vérifiez que le titre de la page est exactement "Example Domain"
# 4. Vérifiez que le contenu contient "Example Domain"
# 5. Fermez le navigateur

from selenium import webdriver
from selenium.webdriver.common.by import By

print("\n" + "=" * 60)
print("Exercice 1")
print("=" * 60)

#Initialiser le driver
driver = webdriver.Chrome()

try:
    print("\n1. Navigation vers example.com...")
    driver.get("https://example.com")
    
    # 3. Vérifiez que le titre de la page est exactement "Example Domain"
    assert driver.title == "Example Domain", f"Titre incorrect : {driver.title}"
    print(f"3. Titre vérifié : {driver.title}")

    # 4. Vérifiez que le contenu contient "Example Domain"
    # Ma solution mais moche car TOUT le code est récupéré, mieux vaut la 4bis
    assert "Example Domain" in driver.page_source, "Texte attendu non trouvé dans le contenu"
    print(f"4. Contenu vérifié : {driver.title}")
    
    #Autre solution : 
    # .text récupère le texte visible de l'élément trouvé.
    body = driver.find_element(By.TAG_NAME, "body")
    assert "Example Domain" in body.text, "Texte attendu non trouvé dans le body"
    print(f"4bis. Contenu vérifié : {body.text}")
    
    
except Exception as e:
    print(f"Erreur d'assertion : {e}")
    
finally:
    # 5. Fermez le navigateur
    print("\n5. Fermeture...")
    driver.quit()
    print("    Fermé")