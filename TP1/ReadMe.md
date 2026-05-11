# TP1 — Contrôle d’accès et vérifications d’interface

## Commande pour lancer le projet :
cd TP1
python main.py

## Objectifs :
Vérifie de façon automatique :
- l’authentification utilisateur sur la page login,
- la vérification d’un écran sécurisé,
- une interaction avec une liste déroulante sur la page dropdown,
- une zone où des éléments sont ajoutés dynamiquement.
Sur le site `https://the-internet.herokuapp.com/`

La validation permet de : 
* réussir la connexion,
* valider le logout,
* valider la sélection dans la liste déroulante,
* valider l’ajout et la suppression dynamique d’éléments.

## Structure du projet :

```text
tp1/
├── pages/
│   ├── login_page.py
│   ├── secure_area_page.py
│   ├── dropdown_page.py
│   └── add_remove_page.py
├── tests/
│   └── test_tp1.py
└── main.py
```

## Les identifiants utilisés sont :

- Username : `tomsmith`
- Password : `SuperSecretPassword!`


## Détails des parties :

### Partie 1 — Authentification
1. Ouvrir la page de login.
2. Vérifier que le titre ou le contenu de la page correspond bien à une page d’authentification.
3. Saisir le username et le password fournis.
4. Cliquer sur le bouton de connexion.
5. Vérifier que la connexion a réussi.
6. Vérifier la présence du message de succès.
7. Vérifier la présence du bouton ou lien de logout.
8. Cliquer sur logout.
9. Vérifier que l’utilisateur revient bien sur la page de login.

### Partie 2 — Liste déroulante
1. Ouvrir la page Dropdown.
2. Vérifier que la liste déroulante est présente.
3. Sélectionner `Option 1`.
4. Vérifier que `Option 1` est bien sélectionnée.
5. Sélectionner ensuite `Option 2`.
6. Vérifier que `Option 2` est bien sélectionnée.

### Partie 3 — Ajout et suppression d’éléments
1. Ouvrir la page Add/Remove Elements.
2. Cliquer 3 fois sur `Add Element`.
3. Vérifier que 3 boutons `Delete` sont affichés.
4. Supprimer 1 élément.
5. Vérifier qu’il reste 2 boutons `Delete`.
6. Supprimer tous les éléments restants.
7. Vérifier qu’il ne reste plus aucun bouton `Delete`.