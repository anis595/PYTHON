from classes.Adresse import Adresse


class Carnet:
    def __init__(self):
        self.list_adress: list[Adresse] = []

    def input_adress(self, addresse: Adresse = None):
        if addresse != None:
            print("====== Modifier une adresse ======")
            print(
                "Veuillez saisir les champs à modifier (entrer pour garder l'ancienne valeur)"
            )

        else:
            print("====== Ajouter une adresse ======")

            numero_voie = input("n° de voie : ") or addresse.numero_voie

            complement = input("Complément : ") or addresse.complement
            intitule = input("Intitulé : ") or addresse.intitule
            commune = input("Commune : ") or addresse.commune
            code_postal = input("Code Postal : ") or addresse.code_postal

        return Adresse(numero_voie, complement, intitule, commune, code_postal)

    def display_adress(self):
        print(" ===== Liste des Adresses =====")
        for adress in self.list_adress:
            print(self.list_adress.index(adress) + 1, end=": ")
            print(adress.afficher())

    def add_adress(self):
        self.list_adress.append(self.input_adress())

    def edit_adress(self):
        self.display_adress()
        index = int(input("Veuillez saisir l'adresse à modifier ")) - 1
        address = self.list_adress[index]
        self.list_adress.pop(index)
        self.list_adress.insert(index, self.input_adress(address))

    def delete_adress(self):
        self.display_adress()
        index = int(input("Veuillez saisir l'adresse à suprimer ")) - 1
