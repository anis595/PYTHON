from classes.Adresse import Adresse
from classes.Carnet import Carnet

carnet = Carnet()


while True:
    print("=== MENU PRINCIPAL ===")
    print("1. Voir les adresses")
    print("2. Ajouter une adresse")
    print("3. Éditer une adresse")
    print("4. Supprimer une adresse")
    print("0. Quitter le programme")
    choix = input("Votre choix : ")
    match choix:
        case "1":
            carnet.display_adress()
        case "2":
            carnet.add_adress()
        case "3":
            carnet.edit_adress()

        case "4":
            carnet.delete_adress()
        case "0":
            exit()
