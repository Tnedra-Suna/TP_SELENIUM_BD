# ### 2. Mettre en place une structure POM
# Créer au moins une classe représentant la page principale du site.
# Cette classe devra permettre de :
# * charger la page ;
# * attendre que les livres soient disponibles ;
# * récupérer les éléments nécessaires à l’extraction.
# ---

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    """Page Object de la main page de books.toscrape.com."""

    # Constantes
    URL = "https://books.toscrape.com"

    # Locators
    BOOK_CARDS = (By.CSS_SELECTOR, "article.product_pod")
    BOOK_TITLE = (By.CSS_SELECTOR, "h3 > a")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_RATING = (By.CSS_SELECTOR, "p.star-rating")
    BOOK_STOCK = (By.CSS_SELECTOR, "p.availability")

    #Constructeur
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait   = WebDriverWait(driver, timeout)

    # * charger la page ;
    def charger(self):
        """Charge la page"""
        self.driver.get(self.URL)
        print("Accédé à books.toscrape.com")

    # * attendre que les livres soient disponibles ;
    def attendre_livres(self):
        """Attend que les livres soient disponibles"""
        self.wait.until(EC.presence_of_all_elements_located(self.BOOK_CARDS))
        print("Livres chargés")


    # * récupérer les éléments nécessaires à l’extraction.
    
    # ### 3. Extraire les données
    # Depuis la page d’accueil, récupérer pour chaque livre affiché les informations utiles.
    # Vous stockerez les données extraites dans une structure adaptée.
    # ---
    def get_livres(self):
        """ Récupére les éléments nécessaires à l’extraction : list de dic"""
        cards = self.driver.find_elements(*self.BOOK_CARDS)
        livres = []

        for card in cards:
            titre  = card.find_element(*self.BOOK_TITLE).get_attribute("title")
            prix   = card.find_element(*self.BOOK_PRICE).text.strip()
            rating = card.find_element(*self.BOOK_RATING).get_attribute("class") #Récup pour le BONUS
            stock  = card.find_element(*self.BOOK_STOCK).text.strip()

            # BONUS note : "star-rating Three" je récup le dernier mot
            note = rating.replace("star-rating", "").strip()

            #La liste de dico
            livres.append({
                "titre": titre,
                "prix":  prix,
                "note":  note,
                "stock": stock,
            })
        return livres
