from classes.Vehicule import Vehicule


class Voiture(Vehicule):
    # Si aucun constructeur dans ma classe, on aura le constructeur de la classe parent.
    def __init__(self, marque, couleur, motirisation, nb_portes):  # < ==constructeur
        super().__init__(marque, couleur, motirisation)
        self.nb_portes = nb_portes

    def afficher(self):
        return f"{super().afficher()}"
