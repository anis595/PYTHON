from classes.Livre import Livre


class Bibliotheque:
    def __init__(self):
        self.list_livre: list[Livre] = []

    def input_livre(self, livre: Livre = None):

        print("====== Ajouter un Livre ======")

        isbn = input("n° ISBN ") or livre.isbn

        titre = input("Titre : ") or livre.titre
        auteur = input("Auteur : ") or livre.auteur
        annee = input("Commune : ") or livre.annee
        dispo = input("Code Postal : ") or livre.disponible

        return Livre(isbn, titre, auteur, annee, dispo)

    def ajouter_livre(self):
        self.list_livre.append(self.input_livre())

    def retirer_livre(self, titre):
        for livre in self.list_livre:
            if livre.titre == titre:
                self.list_livre.remove(livre)

    def afficher_tout(self):
        print(" ===== Liste des Livres =====")
        for livre in self.list_livre:
            print(self.list_livre.index(livre) + 1, end=": ")
            print(livre.afficher())

    def chercher_par_auteur(self, auteur):
        return self.afficher_tout(auteur)

    def nombre_disponible(self):
        return self.list_livre(True)
