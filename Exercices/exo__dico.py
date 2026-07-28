def input_address(address: dict):

    if address != None:
        print(
            "Veuillez saisir les champs à modifier (entrer pour garder l'ancienne valeur)"
        )
    else:
        address = {}

    address["numeroVoie"] = input("N° de voie : ") or address["numeroVoie"]
    address["Complément"] = input("Complément : ") or address["Complément"]
    address["Intitule"] = input("Intitulé : ") or address["Intitule"]
    address["Commune"] = input("Commune : ") or address["Commune"]
    address["CodePostal"] = input("Code Postal : ") or address["CodePostal"]

    return address


def main_menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les adresses")
        print("2. Ajouter une adresse")
        print("3. Éditer une adresse")
        print("4. Supprimer une adresse")
        print("0. Quitter le programme")
        choix = input("Votre choix : ")
        if choix in "12340" and len(choix) == 1:
            return choix
        else:
            print("Erreur, réessayez ! \n")


def user_choice(choix, list_address: list):
    match choix:
        case "1":
            print("=== LISTE DES ADRESSES ===")
            for address in list_address:
                print(list_address.index(address) + 1, end=": ")
                for key, value in address.items():
                    print(f"{key} : {value}", end=", ")
                print()
        case "2":
            list_address.append(input_address())
        case "3":
            nb = int(input("Numéro de l'adresse à modifier : ")) - 1
            address = list_address[nb]
            list_address[nb] = input_address(address)
        case "4":
            nb = int(input("Numéro de l'adresse à supprimer : ")) - 1
            list_address.pop(nb)
        case "0":
            # Si on arrête, on ne renvoie pas la liste car c'est inutile
            return False, None
            # exit()
    # Retourne la variable pour savoir si on continue et notre liste d'adresses mis à jour.
    return True, list_address


def main():
    list_address = [
        {
            "numeroVoie": "59",
            "Complément": "Test1",
            "Intitule": "Test1",
            "Commune": "Test1",
            "CodePostal": "59000",
        }
    ]

    suivant = True

    while suivant:
        choix = main_menu()
        suivant, list_address = user_choice(choix, list_address)


main()
