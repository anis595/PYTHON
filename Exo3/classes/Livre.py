class Livre:
    def __init__(self, isbn, titre, auteur, annee, disponible):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        if self.disponible == False:
            print("Livre pas dispo ")

    def retourne(self):
        pass

    def afficher(self):
        return f" Numéro : {self.isbn}\n Titre : {self.titre}\n Auteur : {self.auteur}\n Année : {self.annee}\n Disponibilité : {self.disponible}  "
