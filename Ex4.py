# **Compétences**: Gérer les dropdowns HTML

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/dropdown
# 3. Localisez le dropdown principal
# 4. Sélectionnez l'option "Option 1"
# 5. Vérifiez que "Option 1" est sélectionné
# 6. Changez pour "Option 2"
# 7. Vérifiez que "Option 2" est maintenant sélectionné
# 8. Fermez le navigateur

# **Validation**:
# - Le dropdown est accessible
# - La sélection change correctement
# - La vérification fonctionne

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

try:
    # 2. Accédez à https://the-internet.herokuapp.com/dropdown
    driver.get("https://the-internet.herokuapp.com/dropdown")
    
    # 3. Localisez le dropdown principal
    dropdown_element = driver.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)
    
    # 4. Sélectionnez l'option "Option 1"
    dropdown.select_by_visible_text("Option 1")
    #dropdown.select_by_value("1")
    
    # 5. Vérifiez que "Option 1" est sélectionné
    selected_option = dropdown.first_selected_option
    selected_text = selected_option.text
    assert selected_text == "Option 1", f"Texte sélectionné incorrect : {selected_text}"
    print(f"5. Option sélectionnée : {selected_text}\n")
    
    # 6. Changez pour "Option 2"
    dropdown.select_by_visible_text("Option 2")
    
    # 7. Vérifiez que "Option 2" est maintenant sélectionné
    selected_option = dropdown.first_selected_option
    selected_text = selected_option.text
    assert selected_text == "Option 2", f"Texte sélectionné incorrect : {selected_text}"
    print(f"6. Option sélectionnée : {selected_text}\n")
    
    # 7bis. Deuxième vérification option 2
    selected_value = selected_option.get_attribute("value")
    assert selected_value == "2", f"Valeur sélectionnée incorrecte : {selected_value}"

    print("Exo 4 OK")

except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("\n6. Fermeture...")
    driver.quit()
    print("    Fermé")