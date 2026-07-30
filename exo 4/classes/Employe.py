class Employe:
    compteur_id = 1

    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire
        self.id_employe = Employe.compteur_id
        Employe.compteur_id += 1

    def presentation(self):
        return f"Je suis {self.nom} mon ID est {self.id_employe} et mon salaire est {self.salaire} € "

    def augmenter_salaire(self, pourcentage):
        self.salaire += self.salaire * (pourcentage / 100)
        return f"Le salaire de {self.nom} à été augmenté de {pourcentage}% il est maintenant de {self.salaire} €"
