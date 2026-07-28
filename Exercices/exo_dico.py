carnet_adresses = [
    {
        "numéro de voie": 20,
        "complément": "impasse",
        "intitulé de voie": "rue motte",
        "commune": "nord",
        "code postal": 59100,
    },
    {
        "numéro de voie": 653,
        "complément": "_",
        "intitulé de voie": "rue billycraford",
        "commune": "sud",
        "code postal": 13000,
    },
    {
        "numéro de voie": 875,
        "complément": "impasse",
        "intitulé de voie": "avenue gibier",
        "commune": "est",
        "code postal": 58964,
    },
]


for addresse in carnet_adresses:
    for key, value in addresse.items():
        print(key, value)


def ajouter_adresse():
    voie = print(input("numéro de voie"))
    complemnt = input("complément")
    intitule = input("intitulé")
    commune = input("commune")
    code_postale = input("code postale")

    nouvelle_adresse = {
        "numéro de voie": voie,
        "complément": complemnt,
        "intitulé de voie": intitule,
        "commune": commune,
        "code postal": code_postale,
    }


# def menu_adre(adresses):
#     while True:
#         print("Faites votre choix :")
#         print("1 - Afficher note minimale")
#         print("2 - Afficher note maximale")
#         print("3 - Afficher moyenne")
#         print("4 - Quitter programme")
#         choix_Menu = input("Votre choix : ")
#         if choix_Menu in "1234" and len(choix_Menu) == 1:
#             pass
#         else:
#             print("Erreur, réessayez !\n")
