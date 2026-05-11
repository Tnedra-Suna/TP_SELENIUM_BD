# ### 4. Générer un rapport
# Afficher dans la console un compte rendu contenant au minimum :
# * le nombre total de livres récupérés ;
# * les informations des premiers livres extraits ;
# * quelques statistiques simples sur les données collectées.
# ---

class Rapport:
    """Class Rapport qui permet de générer et exporter le rapport"""

    #Constructeur
    def __init__(self, livres: list):
        self.livres = livres

    # Fonction qui prend prix string et renvoie prix float
    def conv_prix(self, prix_str: str) -> float:
        """Convertit '£42' en 42"""
        return float(prix_str.replace("£", "").strip())

    def generer_rapport(self, output):
        """Affiche le rapport complet sur la console"""

        print("=" * 60, file=output)    #Envoi dans le txt
        print("=" * 60)                 #Affiche sur la console
        print("TP : EXTRACTION DE DONNÉES DE LIVRES")
        print("=" * 60)

        # * le nombre total de livres récupérés ;
        print("\n--- Phase 2: Extraction des Données ---")
        print(f"{len(self.livres)} livres extraits avec succès")

        # * les informations des premiers livres extraits ;
        for i, livre in enumerate(self.livres, start=1):
            titre_court = (livre["titre"][:20] + " ...") if len(livre["titre"]) > 20 else livre["titre"]
            print(f"Livre {i:>2}: {titre_court} - {livre['prix']} ({livre['note']})")

        # * quelques statistiques simples sur les données collectées.
        print("\n--- Phase 3: Rapport et Statistiques ---")
        print(f"\nNombre total de livres: {len(self.livres)}")

        #Premiers livres
        print("\n5 Premiers Livres:")
        for i, livre in enumerate(self.livres[:5], start=1):
            print(f"  {i}. {livre['titre']}")
            print(f"     Prix: {livre['prix']} | Rating: {livre['note']} | {livre['stock']}")

        # Statistiques prix
        prix_values = [self.conv_prix(l["prix"]) for l in self.livres]
        print("\nStatistiques de Prix:")
        print(f"  Prix moyen:   £{sum(prix_values) / len(prix_values):.2f}")
        print(f"  Prix minimum: £{min(prix_values):.2f}")
        print(f"  Prix maximum: £{max(prix_values):.2f}")

        # Classement par note (merci google)
        from collections import Counter
        distribution = Counter(l["note"] for l in self.livres)
        print("\nDistribution par Note:")
        for note, count in sorted(distribution.items()):
            print(f"  {note} étoiles: {count} livres")

        print("TP RÉUSSI!")
        
            
    def exporter_rapport(self, nom_fichier: str = "rapport_exporte.txt"):
        """Export le rapport complet en txt"""
        import os
               
        os.makedirs(os.path.dirname(nom_fichier), exist_ok=True) if os.path.dirname(nom_fichier) else None

        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            self.generer_rapport(output=fichier)

        print(f"Rapport sauvegardé dans : {os.path.abspath(nom_fichier)}")