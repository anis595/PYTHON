from classes.Vehicule import Vehicule


class Moto(Vehicule):
    def __init__(self, marque, couleur, motirisation, type_moto):
        super().__init__(marque, couleur, motirisation)
        self.type_moto = type_moto

    def afficher(self):
        return f"{super().afficher()} {self.type_moto}"
