class Livre:
    def __init__(self, isbn, titre, auteur, annee):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def emprunter(self):
        if self.disponible == False:
            print("Livre pas dispo ")
    
    def retourne