class Adresse:
    def __init__(self, numero_voie, complement, intitule, commune, code_postal):
        self.numero_voie = numero_voie
        self.complement = complement
        self.intitule = intitule
        self.commune = commune
        self.code_postal = code_postal

    def afficher(self):
        return f"numéro de voie : {self.numero_voie}, complement : {self.complement}, intitulé : {self.intitule}, commune :{self.commune}, code postale : {self.code_postal}"
