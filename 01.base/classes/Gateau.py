class Gateau:
    # constructeur :
    def __init__(
        self, nom_gateau, temps_cuisson, liste_ingredients, etape_recette, nom_createur
    ):
        self.nom_g = nom_gateau
        self.temps = temps_cuisson
        self.liste = liste_ingredients
        self.etape = etape_recette
        self.nom_c = nom_createur

    def teste(self):
        print(f" Liste des ingrédients : {self.liste} ")

    def teste2(self):
        print(f"Les étapes de cuissine : {self.etape} ")

    def affichage(self):
        print(
            f" Nom du gateau :{self.nom_g} \nTemps de cuisson : {self.temps}\nListe d'ingrédients : {self.liste}\nEtape : {self.etape}\nNom du créateur {self.nom_c}\n"
        )
        self.teste
