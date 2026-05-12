import sys, os, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tests.test_login import TestLogin
from tests.test_logout import TestLogout
from tests.test_cart import TestCart
from tests.test_checkout import TestCheckout

from utils.driver_build import get_driver
from utils.screenshot import take_screenshot


def run_tests():
    """Fonction qui lance tous les tests, qui compte les tests réussis et ratés"""
    
    print("=" * 60)
    print("TP3 : Automatisation de tests fonctionnels avec Selenium Python")
    print("=" * 60)
    
    driver = get_driver()
    
    test_login = TestLogin()
    test_cart = TestCart()
    test_checkout = TestCheckout()
    test_logout = TestLogout()
    
    dic_results = {"OK": 0, "FAILED": 0}
    list_tests = [
        ("Scénario 1",     test_login.test_successful_login),
        ("Scénario 2",     test_login.test_locked_out_user_login),
        ("Scénario 3",     test_cart.test_add_product_to_cart),
        ("Scénario 4",     test_checkout.test_complete_purchase),
        ("Scénario 5",     test_logout.test_logout),
    ]
    
    try:
        #Pour chaque tests (fonction) dans list_tests je try ma fonction
        for name, fn in list_tests:
            try:
                fn(driver)
                print(f"--> SUCCÈS — {name}\n")
                dic_results["OK"] += 1
                
            except AssertionError as e:
                print(f"\nÉCHEC assertion de : {name}\n{e}")
                take_screenshot(driver, name)
                dic_results["FAILED"] += 1
                
            except Exception as e:
                print(f"\nERREUR exception — {name}\n       {e}")
                traceback.print_exc()
                take_screenshot(driver, name)
                dic_results["FAILED"] += 1
    finally:
        driver.quit()
        print("Navigateur fermé proprement.")

    print("=" * 60)
    print(f"RÉSULTATS : {dic_results['OK']} réussis / {dic_results['FAILED']} ratés")
    print("=" * 60)
    

if __name__ == "__main__":
    run_tests()