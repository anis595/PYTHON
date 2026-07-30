from classes.Livre import Livre
from classes.Bibliotheque import Bibliotheque

bibliotheque = Bibliotheque("B1")


livre1 = Livre("123", "Le Petit Prince", "Saint-Exupéry", 1943)
livre2 = Livre("456", "Harry Potter", "J.K Rowling", 1997)
livre3 = Livre("789", "Le Seigneur des Anneaux", "J.R.R Tolkien", 1954)

bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)


livre1.emprunter()
livre1.emprunter()
livre1.retourne()
print(livre1.afficher())

bibliotheque.afficher_tout()


print(f"Livres disponibles : {bibliotheque.nombre_disponible()}")

livre_auteur = bibliotheque.chercher_par_auteur("J.K Rowling")

for livre in livre_auteur:
    print(livre.afficher())

bibliotheque.retirer_livre(livre1)

# while True:
#     print("=== MENU PRINCIPAL ===")
#     print("1. Ajouter un Livre")
#     print("2. Retirer un Livre")
#     print("3. Afficher tout les Livres")
#     print("4. Chercher par Auteur")
#     print("5. Disponibilité")
#     print("0. Sorti")
#     choix = input("Votre choix : ")
#     match choix:
#         case "1":
#             bibliotheque.ajouter_livre()
#         case "2":
#             bibliotheque.retirer_livre()
#         case "3":
#             bibliotheque.afficher_tout()

#         case "4":
#             bibliotheque.chercher_par_auteur()
#         case "5":
#             bibliotheque.nombre_disponible()

#         case "0":
#             exit()
