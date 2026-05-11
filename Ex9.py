# **Compétences**: Explicit waits avec WebDriverWait

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/dynamic_loading/1
# 3. Cliquez sur le bouton "Start"
# 4. Attendez explicitement (max 10 secondes) que le texte "Hello World!" apparaisse
# 5. Vérifiez que le texte contient "Hello World!"
# 6. Vérifiez que le texte ne contient pas "It's gone!"
# 7. Fermez le navigateur

# **Validation**:
# - L'attente fonctionne correctement
# - L'élément dynamique est trouvé
# - Le texte est correct

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def exercice9():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 2. Accédez à https://the-internet.herokuapp.com/dynamic_loading/1
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        
        # 3. Cliquez sur le bouton "Start"
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        
        # 4. Attendez explicitement (max 10 secondes) que le texte "Hello World!" apparaisse
        hello_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish")))
     
        # 5. Vérifiez que le texte contient "Hello World!"
        assert "Hello World!" in hello_element.text, f"5. Erreur : le texte ne contient pas 'Hello World!' : {hello_element.text}"
        
        # 6. Vérifiez que le texte ne contient pas "It's gone!"
        assert "It's gone!" not in hello_element.text, f"6. Erreur : le texte contient 'It's gone!' : {hello_element.text}"

        print("Exercice 9 OK")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("\n6. Fermeture...")
        driver.quit()
        print("    Fermé")


if __name__ == "__main__":
    exercice9()