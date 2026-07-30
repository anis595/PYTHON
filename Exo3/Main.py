from classes.Livre import Livre
from classes.Bibliotheque import Bibliotheque

bibliotheque = Bibliotheque()


while True:
    print("=== MENU PRINCIPAL ===")
    print("1. Ajouter un Livre")
    print("2. Retirer un Livre")
    print("3. Afficher tout les Livres")
    print("4. Chercher par Auteur")
    print("5. Disponibilité")
    print("0. Sorti")
    choix = input("Votre choix : ")
    match choix:
        case "1":
            bibliotheque.ajouter_livre()
        case "2":
            bibliotheque.retirer_livre()
        case "3":
            bibliotheque.afficher_tout()

        case "4":
            bibliotheque.chercher_par_auteur()
        case "5":
            bibliotheque.nombre_disponible()

        case "0":
            exit()
