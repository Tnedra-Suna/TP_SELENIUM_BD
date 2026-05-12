# TP 3 — Automatisation de tests fonctionnels avec Selenium Python

## Commande pour lancer le projet :

`cd TP3`
`main.py`

## Installation :

`python -m venv venv`
`source venv/bin/activate`
`pip install -r requirements.txt`

## Objectifs :
* automatiser plusieurs scénarios utilisateur ;
* utiliser Selenium avec Python ;
* mettre en place le Page Object Model (POM) ;
* utiliser des attentes explicites ;
* générer des logs ;
* effectuer des captures d’écran ;
* structurer correctement un repository GitHub.

## Structure du projet :

```text
TP3/
├── README.md
├── requirements.txt
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_complete_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
├── utils/
│   ├── driver_build.py
│   ├── logger.py
│   └── screenshot.py
├── logs/   
└── screenshots/
```

## Site testé :

[Sauce Demo](https://www.saucedemo.com/)

### Informations client utilisées :

```text
Prénom : John
Nom : Doe
Code postal : 59000
```

## Détails des parties :

## Scénario 1 — Connexion réussie

```text
Utilisateur : standard_user
Mot de passe : secret_sauce
```
Résultat :

* l’utilisateur accède à la page catalogue ;
* le titre de la page inventaire est visible.

---

## Scénario 2 — Connexion refusée

```text
Utilisateur : locked_out_user
Mot de passe : secret_sauce
```

Résultat :

* un message d’erreur est affiché ;
* l’utilisateur reste sur la page de connexion.

---

## Scénario 3 — Ajout d’un produit au panier

Après connexion avec `standard_user`, ajouter le produit suivant :

```text
Sauce Labs Backpack
```

Résultats :

* le bouton du produit passe de `Add to cart` à `Remove` ;
* l’icône du panier affiche `1` ;
* le panier contient bien `Sauce Labs Backpack` ;
* le prix affiché dans le panier correspond au prix du produit sélectionné.

Screenshot demandé :

* effectuer une capture d’écran après l’ajout du produit au panier.

---

## Scénario 4 — Parcours d’achat complet

1. connexion ;
2. ajout du produit `Sauce Labs Backpack` ;
3. ouverture du panier ;
4. vérification du produit présent dans le panier ;
5. démarrage du checkout ;
6. saisie des informations client ;
7. vérification du récapitulatif ;
8. validation de la commande.

Résultats :

* le récapitulatif contient bien `Sauce Labs Backpack` ;
* le prix du produit est correct ;
* le total hors taxe correspond au prix du produit ;
* la taxe est affichée ;
* le total final est cohérent ;
* le message suivant est affiché après validation :

```text
Thank you for your order!
```

* capture d’écran de la page de confirmation finale.

---

## Scénario 5 — Déconnexion

Après connexion avec `standard_user`, automatiser la déconnexion.

Résultat :

* l’utilisateur revient sur la page de login.

---




