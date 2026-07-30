class Vehicule:
    def __init__(self, marque, couleur, motirisation):
        self.marque = marque
        self.couleur = couleur
        self.motirisation = motirisation

    def demarrer(self):
        return f"{self.marque} démarre "

    def afficher(self):
        return f"{self.marque} - couleur : {self.couleur} Moteur : {self.motirisation} "
