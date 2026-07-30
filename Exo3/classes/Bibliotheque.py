from classes.Livre import Livre


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres: list[Livre] = []

    # def input_livre(self, livre: Livre = None):

    #     print("====== Ajouter un Livre ======")

    #     isbn = input("n° ISBN ") or livre.isbn

    #     titre = input("Titre : ") or livre.titre
    #     auteur = input("Auteur : ") or livre.auteur
    #     annee = input("Commune : ") or livre.annee
    #     dispo = input("Code Postal : ") or livre.disponible

    #     return Livre(isbn, titre, auteur, annee, dispo)

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

    def retirer_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                choix = input(f" Voulez vous supprimer le livre ?  (Y/N)")
                print(livre.afficher())
                if choix.lower() == "Y":
                    self.livres.remove(livre)
                    print("livre supprimé")
                else:
                    print("abandon")

    def afficher_tout(self):
        print(" ===== Liste des Livres =====")
        for livre in self.livres:
            print(livre.afficher())

    def chercher_par_auteur(self, auteur):
        # return self.afficher_tout(auteur)
        resultat = []
        for livre in self.livres:
            if livre.auteur == auteur:
                resultat.append(livre)
            return resultat

        # return[livre for livre in self.livres if livre.auteur == auteur]

    def nombre_disponible(self):
        count = 0
        for livre in self.livres:
            if livre.disponible:
                count += 1
        return count
