class Chien:
    # constructeur :
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        print(f"{self.nom} waf waf ")

    def aboyer_sur(self, chien):
        print(f"{self.nom} aboie sur {chien.nom}")
