# # TP2 — Tester des contenus dynamiques avec Selenium

import sys, os, traceback
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page  import DynamicLoadingPage
from pages.notification_page     import NotificationPage
from pages.infinite_scroll_page  import InfiniteScrollPage
from utils import log, assert_true, screenshot_on_error, build_driver


# ### Partie 1 — Dynamic Controls
def test_dynamic_controls(driver):
    print("=" * 60)
    print("  PARTIE 1 — Dynamic Controls")
    print("=" * 60)
    
    page = DynamicControlsPage(driver)

    # 1. Ouvrir la page Dynamic Controls.
    # 2. Vérifier que la page est bien chargée.
    log("Ouverture de la page Dynamic Controls...")
    page.open()
    
    # 3. Vérifier que la case à cocher est présente.
    assert_true(page.is_checkbox_present(), "Case à cocher présente !", "Case à cocher introuvable")
    
    # 4. Cliquer sur `Remove`.
    log("Clic sur Remove...")
    page.click_remove_add()
    
    # 5. Attendre correctement la disparition de la case à cocher.
    page.wait_checkbox_removed()
    
    # 6. Vérifier le message de confirmation affiché.
    assert_true(not page.is_checkbox_present(), "Case à cocher disparue", "Case encore présente") 
    msg = page.get_result_message()
    assert_true("It's gone!" in msg, f"Message après Remove : '{msg}'", f"Message inattendu : '{msg}'")
    
    # 7. Cliquer sur `Add`.
    log("Clic sur Add...")
    page.click_remove_add()
    
    # 8. Attendre correctement la réapparition de la case à cocher.
    page.wait_checkbox_added()
    
    # 9. Vérifier le nouveau message de confirmation.
    assert_true(page.is_checkbox_present(), "Case à cocher réapparue", "La case n'est pas réapparue")
    msg = page.get_result_message()
    assert_true("It's back!" in msg, f"Message après Add : '{msg}'", f"Erreur, message inattendu : '{msg}'")
    
    # 10. Dans la zone `Enable/disable`, vérifier que le champ texte est initialement désactivé.
    assert_true(page.is_input_disabled(), "Champ texte initialement désactivé", "Problème : le champ devrait être désactivé")
    
    # 11. Cliquer sur `Enable`.
    log("Clic sur Enable...")
    page.click_enable_disable()
    
    # 12. Attendre correctement que le champ devienne actif.
    page.wait_input_enabled()
    
    # 13. Vérifier qu’il est maintenant possible d’écrire dedans.
    assert_true(not page.is_input_disabled(), "Champ texte activé", "Problème : le champ est encore désactivé")
    
    # 14. Saisir un texte de test et vérifier qu’il a bien été saisi.
    test_text = "C'est le TP2 de Benjam"
    page.type_in_input(test_text)
    value = page.get_input_value()
    assert_true(value == test_text, f"Texte saisi : '{value}'", f"Attendu '{test_text}', trouvé '{value}'")


# ### Partie 2 — Dynamic Loading
def test_dynamic_loading(driver):
    print("=" * 60)
    print("  PARTIE 2 — Dynamic Loading")
    print("=" * 60)
    
    page = DynamicLoadingPage(driver)

    # 1. Ouvrir la page Dynamic Loading.
    # 2. Aller sur `Example 2: Element rendered after the fact`.
    log("Ouverture de 'Example 2'...")
    page.open_example_2()
       
    # 3. Vérifier que le bouton `Start` est présent.
    assert_true(page.is_start_button_present(), "Bouton Start présent", "Bouton Start absent")
    
    # 4. Cliquer sur `Start`.
    log("Clic sur Start — attente du contenu dynamique...")
    page.click_start()
    
    # 5. Attendre correctement l’apparition du contenu chargé dynamiquement.
    text = page.wait_for_content()
    
    # 6. Vérifier que le texte `Hello World!` apparaît bien.
    assert_true("Hello World!" in text, f"Texte ok : '{text}'", f"Texte inattendu : '{text}'")


# ### Partie 3 — Notification Message
def test_notification_message(driver):
    print("=" * 60)
    print("  PARTIE 3 — Notification Message")
    print("=" * 60)
    
    page = NotificationPage(driver)

    # 1. Ouvrir la page Notification Message.
    log("Ouverture de la page...")
    page.open()
    
    # 2. Lire le message affiché.
    initial_msg = page.click_and_get_message()
    assert_true(bool(initial_msg), "Message initial présent", "Aucun message affiché")
    
    # 3. Cliquer sur `Click here` pour charger une nouvelle notification.
    # 5. Répéter l’action plusieurs fois.
    for i in range(1, 4):
        log(f"Clic numéro : {i}...")
        msg = page.click_and_get_message()
        
        # 4. Vérifier qu’un message est bien affiché après le clic.
        assert_true(bool(msg), f"Message après clic numéro {i} : '{msg}'", f"Aucun message après clic numéro {i}")
        
        # 6. Vérifier que le message obtenu appartient bien aux messages attendus.
        assert_true(page.is_valid_message(msg), f"Message valide : '{msg}'", f"Message inattendu : '{msg}'")
    
    
# ### Partie 4 — Infinite Scroll
def test_infinite_scroll(driver):
    print("=" * 60)
    print("  PARTIE 4 — Infinite Scroll")
    print("=" * 60)
    
    page = InfiniteScrollPage(driver)

    # 1. Ouvrir la page Infinite Scroll.
    log("Ouverture de la page...")
    page.open()
    
    # 2. Vérifier qu’un premier bloc de texte est présent.
    initial_count = page.get_paragraph_count()
    assert_true(initial_count > 0, f"Contenu initial : {initial_count} bloc(s)", "Aucun bloc trouvé")
    log(f"Blocs avant scroll : {initial_count} — scrollage...")
    
    # 3. Faire défiler la page plusieurs fois vers le bas.
    page.scroll_down(times=3, pause=1)
    
    # 4. Vérifier qu’un contenu supplémentaire apparaît après le scroll.
    # 5. Compter le nombre de blocs visibles avant et après le scroll.
    # 6. Vérifier que ce nombre a augmenté.
    new_count = page.wait_more_content(initial_count)
    assert_true(new_count > initial_count, f"Nouveau contenu passant de ({initial_count} à {new_count} blocs)", f"Aucun nouveau bloc avant : {initial_count} après : {new_count})")
    
        
def run_tests():
    """Fonction qui lance tous les tests, qui compte les tests réussis et ratés"""
    
    print("=" * 60)
    print("TP2 : lancement de tous les tests")
    print("=" * 60)
    
    driver = build_driver()
    dic_results = {"OK": 0, "FAILED": 0}
    list_tests = [
        ("Dynamic Controls",     test_dynamic_controls),
        ("Dynamic Loading",      test_dynamic_loading),
        ("Notification Message", test_notification_message),
        ("Infinite Scroll",      test_infinite_scroll),
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