from classes.Employe import Employe


class Technicien(Employe):
    def __init__(self, nom, salaire, specialite):
        super().__init__(nom, salaire)
        self.specialite = specialite

    def changer_specialite(self, new_specialite):
        self.specialite = new_specialite
