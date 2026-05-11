# **Compétences**: Gérer les checkboxes

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/checkboxes
# 3. Localisez les checkboxes
# 4. Vérifiez l'état initial des cases
# 5. Cochez la première case si elle n'est pas cochée
# 6. Vérifiez que la première case est maintenant cochée
# 7. Décochez la deuxième case si elle est cochée
# 8. Vérifiez que la deuxième case est décochée
# 9. Fermez le navigateur

# **Validation**:
# - L'état initial est vérifié
# - La case se coche/décoche correctement
# - La vérification de l'état fonctionne

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    
    # 2. Accédez à https://the-internet.herokuapp.com/checkboxes
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    
    # 3. Localisez les 2 checkboxes
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert len(checkboxes) == 2, f"Nombre de checkboxes inattendu : {len(checkboxes)}"

    # 4. Vérifiez l'état initial des cases
    checkbox_1 = checkboxes[0]
    checkbox_2 = checkboxes[1] 
    assert not checkbox_1.is_selected(), "La checkbox 1 devrait être décochée au départ"
    print("4. La checkbox 1 est bien décochée au départ")
    assert checkbox_2.is_selected(), "La checkbox 2 devrait être cochée au départ"
    print("4. La checkbox 2 est bien cochée au départ")
    
    # 5. Cochez la première case si elle n'est pas cochée
    if not checkbox_1.is_selected():
        checkbox_1.click()
    
    # 6. Vérifiez que la première case est maintenant cochée
    assert checkbox_1.is_selected(), "La checkbox 1 devrait être cochée maintenant"
    print("6. La checkbox 1 est maintenant cochée")
    
    # 7. Décochez la deuxième case si elle est cochée
    if checkbox_2.is_selected():
        checkbox_2.click()
    
    # 8. Vérifiez que la deuxième case est décochée
    assert not checkbox_2.is_selected(), "La checkbox 2 devrait être décochée maintenant"
    print("8. La checkbox 2 est maintenant décochée")

    print("Exercice 5 OK")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("\n6. Fermeture...")
    driver.quit()
    print("    Fermé")