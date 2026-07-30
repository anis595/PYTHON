class CompteBancaire:
    def __init__(self, numero_compte, nom, solde):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde

    def versement(self, montant):
        if montant < 0:
            print("Veuillez saisir un montant positif")
        else:
            self.solde += montant
            self.afficher()

    def retrait(self, montant):
        if montant > 0:
            print("Veuillez saisir un montant négatif")
        else:
            self.solde += montant
            self.afficher()

    def afficher(self):
        print(f"compte bancaire numéro : {self.numero_compte}")
        print(f"Appartient à : {self.nom}")
        print(f"solde : {self.solde} €")

    def agios(self):
        if self.solde < 0:
            montant = self.solde * 0.05
            self.afficher()
