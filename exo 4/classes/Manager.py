from classes.Employe import Employe


class Manager(Employe):
    def __init__(self, nom, salaire, equipe):
        super().__init__(nom, salaire)
        self.equipe = equipe

    def ajouter_employe(self, employe):
        self.equipe.append(employe)

    def presentation_m(self):
        count = 0
        for employe in self.equipe:
            count += 1
        return f"Je suis {self.nom}, manager. Mon ID est {self.id_employe}Je supervise une équipe de {count} personnes et mon salaire est de{self.salaire} €"
