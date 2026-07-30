class Livre:
    def __init__(self, isbn, titre, auteur, annee):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f" {self.titre} est déjà emprunté !")

    def retourne(self):
        self.disponible = True

    def afficher(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f" Numéro : {self.isbn}\n Titre : {self.titre}\n Auteur : {self.auteur}\n Année : {self.annee}\n Disponibilité : {statut}  "
