# **Compétences**: Remplir un champ texte, soumettre

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://demoqa.com/text-box
# 3. Remplissez le champ "Full Name" avec "John Doe"
# 4. Remplissez le champ "Email" avec "john@example.com"
# 5. Remplissez le champ "Current Address" avec "123 Main Street"
# 6. Cliquez sur le bouton "Submit"
# 7. Vérifiez que les données sont affichées dans le résultat
# 8. Fermez le navigateur

# **Validation**:
# - Le formulaire est rempli correctement
# - La soumission fonctionne
# - Les données sont affichées dans la zone de résultat

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# WebDriverWait permet d'attendre qu'une condition soit remplie
# pendant un certain temps avant de déclencher une erreur.
wait = WebDriverWait(driver, 10)

try:
    # 2. Accédez à https://demoqa.com/text-box
    driver.get("https://demoqa.com/text-box")

    # 3. Remplissez le champ "Full Name" avec "John Doe"
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("John Doe")
    
    # 4. Remplissez le champ "Email" avec "john@example.com"
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("john@example.com")
    
    # 5. Remplissez le champ "Current Address" avec "123 Main Street"
    address_field = driver.find_element(By.ID, "currentAddress")
    address_field.send_keys("123 Main Street")
    
    # 6. Cliquez sur le bouton "Submit"
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    # 7. Vérifiez que les données sont affichées dans le résultat
    wait.until(EC.presence_of_element_located((By.ID, "output")))
    output = driver.find_element(By.ID, "output")
    output_text = output.text

    assert "John Doe" in output_text, "Nom non trouvé dans le résultat"
    assert "john@example.com" in output_text, "Email non trouvé dans le résultat"
    assert "123 Main Street" in output_text, "Adresse non trouvée dans le résultat"
    
    print(f"Résultat vérifié :\n{output_text}")


except Exception as e:
    print(f"Erreur : {e}")

finally:
    print("\n6. Fermeture...")
    driver.quit()
    print("    Fermé")