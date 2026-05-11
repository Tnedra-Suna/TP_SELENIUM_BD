#Vérif :
# - de l’authentification utilisateur,
# - de la vérification d’un écran sécurisé,
# - d’une interaction avec une liste déroulante,
# - d’une zone où des éléments sont ajoutés dynamiquement.

# - Base URL : `https://the-internet.herokuapp.com/`

# - Login : `https://the-internet.herokuapp.com/login`
# - Dropdown : `https://the-internet.herokuapp.com/dropdown`
# - Add/Remove Elements : `https://the-internet.herokuapp.com/add_remove_elements/`

# ## Contraintes techniques

# Vous devez obligatoirement :

# - utiliser le **Page Object Model** ;
# - séparer les pages dans des classes différentes ;
# - éviter de mettre toute la logique dans un seul fichier ;
# - utiliser des méthodes explicites et lisibles ;
# - prévoir au minimum quelques assertions ;
# - fermer le navigateur proprement à la fin.


# Le scénario complet doit :

# * réussir la connexion,
# * valider le logout,
# * valider la sélection dans la liste déroulante,
# * valider l’ajout et la suppression dynamique d’éléments.

#À l’exécution, le script doit afficher clairement les étapes e

# ## Bonus

# Si vous terminez en avance, ajoutez :

# * des messages de log simples ;
# * une méthode utilitaire pour éviter de dupliquer certaines vérifications.

"""
# test_tp1.py : TP1 — Contrôle d’accès et vérifications d’interface
"""

import os
import datetime
import traceback
import sys
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Pour indiquer où chercher les dossiers de TP1
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#Optimisation à faire avec __init__.py ?
from pages.login_page       import LoginPage
from pages.secure_area_page import SecureAreaPage
from pages.dropdown_page    import DropdownPage
from pages.add_remove_page  import AddRemovePage

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

#Identifiants à utiliser
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"


#Affichage message
def log(msg: str):
    #print(msg)
    logger.info(msg)

#À l’exécution, le script doit afficher clairement si les vérifications sont réussies ou non.
def assert_true(condition: bool, ok_msg: str, fail_msg: str):
    """Fonction résultat assertion : succès ou échec"""
    if condition:
        print(f"REUSSI : {ok_msg}")
    else:
        raise AssertionError(f"ECHEC : {fail_msg}")

# * une capture d’écran en cas d’erreur ;
def screenshot_on_error(driver, test_name: str):
    """Une capture d’écran en cas d’erreur"""
    os.makedirs("screenshots", exist_ok=True)    
    screenshot_name = f"screenshots/{test_name.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(screenshot_name)
    print(f" Screenshot sauvegardé: {screenshot_name}")

#Gère les options du navigateur
def build_driver() -> webdriver.Chrome:
    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--window-size=1920,1080")
    
    # Préférences internes de Chrome
    # Elles permettent notamment d'éviter des alertes liées aux mots de passe
    prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    # Ajoute les préférences Chrome à la configuration du navigateur
    options.add_experimental_option("prefs", prefs)
        
    return webdriver.Chrome(options=options)


# ### Partie 1 — Authentification
def test_authentification(driver):
    print("=" * 60)
    print("PARTIE 1 — Authentification")
    print("=" * 60)

    #Création des pages
    login_page  = LoginPage(driver)
    secure_page = SecureAreaPage(driver)

    # 1. Ouvrir la page de login.
    log("Ouverture de la page de login...")
    login_page.open()
    
    # 2. Vérifier que le titre ou le contenu de la page correspond bien à une page d’authentification.
    heading = login_page.get_heading_text()
    assert_true("Login Page" in heading, f"Titre correct : '{heading}'", f"Titre incohérent, titre trouvé : '{heading}'")
    
    # 3. Saisir le username et le password fournis.
    # 4. Cliquer sur le bouton de connexion.
    log(f"Connexion avec les id de '{USERNAME}'...")
    login_page.login(USERNAME, PASSWORD)
    
    # 5. Vérifier que la connexion a réussi. (et qu'on est sur la page secure)
    secure_heading = secure_page.get_heading_text()
    assert_true("Secure Area" in secure_heading, "La page est sécurisée", f"Page non sécurisée, affichage réel : '{secure_heading}'")
    
    # 6. Vérifier la présence du message de succès.
    flash = secure_page.get_flash_message()
    assert_true("You logged into a secure area" in flash, f"Message bien affiché : '{flash.strip()}'", f"Pas de message succès, message trouvé : '{flash}'")
    
    # 7. Vérifier la présence du bouton ou lien de logout.
    assert_true(secure_page.is_logout_button_present(), "Bouton Logout affiché", "Bouton Logout introuvable")
    
    # 8. Cliquer sur logout.
    log("Clic sur Logout...")
    secure_page.click_logout()
    
    # 9. Vérifier que l’utilisateur revient bien sur la page de login.
    login_heading = login_page.get_heading_text()
    assert_true("Login Page" in login_heading, "Retour sur la page de login confirmé après logout", f"Redirection inattendue. Titre : '{login_heading}'")
    
    
# ### Partie 2 — Liste déroulante
def test_dropdown(driver):
    print("=" * 60)
    print("PARTIE 2 — Liste déroulante")
    print("=" * 60)

    page = DropdownPage(driver)

    # 1. Ouvrir la page Dropdown.
    log("Ouverture de la page Dropdown...")
    page.open()
    
    # 2. Vérifier que la liste déroulante est présente.
    assert_true(page.is_dropdown_present(), "Liste déroulante présente", "Liste déroulante introuvable")
    
    # 3. Sélectionner `Option 1`.
    log("Sélection de 'Option 1'...")
    page.select_option_by_text("Option 1")
        
    # 4. Vérifier que `Option 1` est bien sélectionnée.
    selected = page.get_selected_option_text()
    assert_true(selected == "Option 1", f"'Option 1' sélectionnée (valeur : '{selected}')", f"Attendu 'Option 1', trouvé '{selected}'")
    
    # 5. Sélectionner ensuite `Option 2`.
    log("Sélection de 'Option 2'...")
    page.select_option_by_text("Option 2")
    
    # 6. Vérifier que `Option 2` est bien sélectionnée.  
    selected = page.get_selected_option_text()
    assert_true(selected == "Option 2", f"'Option 2' sélectionnée (valeur : '{selected}')", f"Attendu 'Option 2', trouvé '{selected}'")
    

# ### Partie 3 — Ajout et suppression d’éléments
def test_add_remove_elements(driver):
    print("=" * 60)
    print("Partie 3 — Ajout et suppression d’éléments")
    print("=" * 60)

    page = AddRemovePage(driver)

    # 1. Ouvrir la page Add/Remove Elements.
    log("Ouverture de la page Add/Remove Elements...")
    page.open()
    
    # 2. Cliquer 3 fois sur `Add Element`.
    log("Cliquer 3 fois...")
    for _ in range(3):
        page.click_add_element()
        
    # 3. Vérifier que 3 boutons `Delete` sont affichés.
    count_delete = page.get_delete_button_count()
    assert_true(count_delete == 3, f"3 boutons Delete", f"Attendus 3, trouvés {count_delete}")
    
    # 4. Supprimer 1 élément.
    log("Suppression de 1 élément...")
    page.click_first_delete_button()
    
    # 5. Vérifier qu’il reste 2 boutons `Delete`.
    count_delete = page.get_delete_button_count()
    assert_true(count_delete == 2, f"2 boutons Delete", f"Attendus 2, trouvés {count_delete}")
    
    # 6. Supprimer tous les éléments restants.
    log("Supprimer tous les éléments restants...")
    page.delete_all_elements()
    
    # 7. Vérifier qu’il ne reste plus aucun bouton `Delete`.  
    count_delete = page.get_delete_button_count()
    assert_true(count_delete == 0, "Aucun bouton Delete", f"Des boutons sont encore là : {count_delete}")


#Fonction qui lance tous les tests, qui compte les tests réussis et ratés
def run_tests():
    """Fonction qui lance tous les tests, qui compte les tests réussis et ratés"""
    
    print("=" * 60)
    print("TP1 : lancement de tous les tests")
    print("=" * 60)

    driver = build_driver()
    dic_results = {"OK": 0, "FAILED": 0}

    #Appel des méthodes dans une liste de tuple
    list_tests = [
        ("Authentification",             test_authentification),
        ("Liste déroulante",             test_dropdown),
        ("Ajout / Suppression éléments", test_add_remove_elements),
    ]

    try:
        #Pour chaque tests (fonction) dans list_tests je try ma fonction
        for name, fn in list_tests:
            try:
                fn(driver)
                print(f"\nSUCCÈS — {name}")
                dic_results["OK"] += 1
                
            except AssertionError as e:
                print(f"\nÉCHEC assertion de : {name}\n{e}")
                screenshot_on_error(driver, name)
                dic_results["FAILED"] += 1
                
            except Exception as e:
                print(f"\nERREUR exception — {name}\n       {e}")
                traceback.print_exc()
                screenshot_on_error(driver, name)
                dic_results["FAILED"] += 1
    finally:
        driver.quit()
        log("Navigateur fermé proprement.")

    print("=" * 60)
    print(f"RÉSULTATS : {dic_results['OK']} réussis / {dic_results['FAILED']} ratés")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()