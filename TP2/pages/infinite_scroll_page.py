#### Partie 4 — Infinite Scroll

import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    URL = "https://the-internet.herokuapp.com/infinite_scroll"

    PARAGRAPHS = (By.CSS_SELECTOR, ".jscroll-added")

    # 1. Ouvrir la page Infinite Scroll.
    def open(self):
        super().open(self.URL)
        self.wait_present(self.PARAGRAPHS)

    # 2. Vérifier qu’un premier bloc de texte est présent.
    # 5. Compter le nombre de blocs visibles avant et après le scroll.
    # 6. Vérifier que ce nombre a augmenté.
    def get_paragraph_count(self) -> int:
        return len(self.find_all(self.PARAGRAPHS))

    # 3. Faire défiler la page plusieurs fois vers le bas.
    def scroll_down(self, times: int = 3, pause: float = 1.5):
        """Scrolle vers le bas plusieurs fois et attend le chargement JS."""
        for _ in range(times):
            self.scroll_to_bottom()
            time.sleep(pause)  # nécessaire : pas d'élément précis à attendre

    # 4. Vérifier qu’un contenu supplémentaire apparaît après le scroll.
    def wait_more_content(self, initial_count: int) -> int:
        """Attend que le nombre de paragraphes dépasse initial_count."""
        self.wait.until(
            lambda d: len(d.find_elements(*self.PARAGRAPHS)) > initial_count
        )
        return self.get_paragraph_count()