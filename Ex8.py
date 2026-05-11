# **Compétences**: Accepter/refuser les alertes

# **Instructions**:
# 1. Ouvrez le navigateur
# 2. Accédez à https://the-internet.herokuapp.com/javascript_alerts
# 3. Cliquez sur "Click for JS Alert"
# 4. Acceptez l'alerte (OK)
# 5. Vérifiez le message affiché après l'acceptation
# 6. Cliquez sur "Click for JS Confirm"
# 7. Refusez l'alerte (Cancel)
# 8. Vérifiez le message de refus
# 9. Fermez le navigateur

# **Validation**:
# - Les alertes sont gérées correctement
# - Les messages de confirmation/refus sont corrects

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def exercice8():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 2. Accédez à https://the-internet.herokuapp.com/javascript_alerts
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        
        # 3. Cliquez sur "Click for JS Alert"
        # On déclenche un contenu qui apparaît après un délai.
        driver.find_element(By.CSS_SELECTOR, 'button[onclick="jsAlert()"]').click()
     
        # 4. Acceptez l'alerte (OK)
        # alert_is_present() attend qu'une alerte JavaScript soit réellement ouverte.
        alert = wait.until(EC.alert_is_present())
        # .text lit le message affiché dans l'alerte.
        assert alert.text == "I am a JS Alert", f"4. Alerte inattendue : {alert.text}"
        # accept() correspond au bouton OK.
        alert.accept()
        
        # 5. Vérifiez le message affiché après l'acceptation
        result = driver.find_element(By.ID, "result")
        assert result.text == "You successfully clicked an alert", f"5. Alerte inattendue : {result.text}"
        
        # 6. Cliquez sur "Click for JS Confirm"
        driver.find_element(By.CSS_SELECTOR, 'button[onclick="jsConfirm()"]').click()
        alert_result = wait.until(EC.alert_is_present())
        assert alert_result.text == "I am a JS Confirm", f"6. Confirmation inattendue : {alert_result.text}"
        
        # 7. Refusez l'alerte (Cancel) : dismiss() correspond au bouton Annuler / Cancel.
        alert.dismiss()
        
        # 8. Vérifiez le message de refus
        alert_result = driver.find_element(By.ID, "result")
        assert alert_result.text == "You clicked: Cancel", f"Résultat confirmation incorrect : {alert_result.text}"

        print("Exercice 8 OK \U0001F44B")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        print("\n6. Fermeture...")
        driver.quit()
        print("    Fermé")

    

if __name__ == "__main__":
    exercice8()