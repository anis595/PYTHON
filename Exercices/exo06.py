# notes_clients = [12, 4, 18, 9, 15, 7, 19, 11]

# for note in notes_clients:
#     if note > 10:
#         print(note, "OK")

# mot_de_passe = input("veuillez saisir votre mdp: ")

# while mot_de_passe != "data2026":
#     mot_de_passe = input("veuillez saisir votre mdp: ")
#     if mot_de_passe == "data2026":
#         print("mot de passe correct")


# releves = [12, -4, 55, 3, -60, 8, 48, -12, 105]

# for releve in releves:
#     if -50 <= releve <= 50:
#         print(releve)


# prix_articles = [15.99, -5.0, 45.50, 0.0, 120.0, 8.50, -2.5, 99.99]

# for prix in prix_articles:
#     if prix > 0:
#         print(prix)

# notes_etudiants = [8.5, 12.0, 16.5, 9.0, 14.2, 7.5, 10.0, 19.0]

# for notes in notes_etudiants:
#     if notes >= 10:
#         print(notes, "réussi")
#     if notes < 10:
#         print(notes, "raté")


# nombres = [4, 7, 12, 19, 22, 33, 40, 55]

# for nb in nombres:
#     if nb % 2 == 0:
#         print(nb)

# quantites = [2, 15, 4, 30, 8, 50, 1, 12]

# for quantite in quantites:
#     if quantite > 10 and quantite % 2 == 0:
#         print(quantite)

# stocks = [5, 12, 0, 45, 8, 22, 100, 3]

# for st in stocks:
#     if st < 5:
#         print("Alerte critique", st)
#     elif st >= 5 and st < 20:
#         print("Stock normal", st)
#     else:
#         print("Surstock", st)


# mots = ["chat", "ordinateur", "python", "sql", "donnees", "ia", "analyse"]

# for mot in mots:
#     if len(mot) > 3:
#         print(mot)

# mots_cles = ["data", "sql", "python", "intelligence", "analyse", " BI", "dashboard"]
# compteur = 0

# for mt in mots_cles:
#     if len(mt) > 5:
#         print(mt)
#         compteur = compteur + 1


# print(compteur)


# catalogue = [
#     {"nom": "Clavier", "prix": 25},
#     {"nom": "Écran", "prix": 150},
#     {"nom": "Souris", "prix": 15},
#     {"nom": "PC Portable", "prix": 800},
#     {"nom": "Tapis de souris", "prix": 8},
# ]

# for produit in catalogue:
#     if produit["prix"] >= 50:
#         print(produit["nom"])


# nombres = [12, 45, 7, 89, 23]
# compteur = 0

# for nb in nombres:
#     if nb > 12:
#         print(nb)
#         compteur = compteur + 1

# print(compteur)

# nombres = [5, 22, 10, 45, 3]
# compteur = 0

# for nb in nombres:
#     if nb > 5:
#         print("ko", nb)
#         compteur = compteur + 1

# print(compteur)

# nombres = [8, 42, 15, 99, 23, 7]
# plus_grand = nombres[0]

# for nb in nombres:
#     if nb > plus_grand:
#         plus_grand = nb


# print(plus_grand)


# nombres = [45, 12, 89, 3, 23, 7]
# plus_petit = nombres[0]

# for nb in nombres:
#     if nb < plus_petit:
#         plus_petit = nb

# print(plus_petit)


# notes = [12, 15, 8, 20, 10]
# total = 0

# for note in notes:
#     total = total + note

# moyenne = total / len(notes)


# print(moyenne)


# paniers = [12, 65, 34, 89, 22, 150, 45, 9]
# compteur = 0

# for panier in paniers:
#     if panier > 50:
#         print(panier)
#         compteur = compteur + 1
# print(compteur)

# notes_examen = [8, 14, 10, 19, 5, 12, 7, 16]
# compteur = 0

# for note in notes_examen:
#     if note >= 10:
#         print(note, "Félicitation")
#         compteur = compteur + 1
# print(compteur)

# ventes_brutes = [12, 0, 45, -10, 89, 5, 0, 300, 15]
# tiny_vente = 0
# plus_grand = ventes_brutes[0]
# total = 0


# for vente in ventes_brutes:
#     if vente > 0:
#         total = total + vente
#         moyenne = total / len(ventes_brutes)
#         if vente < 50:
#             tiny_vente = tiny_vente + 1
#         if vente > plus_grand:
#             plus_grand = vente


# print("la plus grosse vente est : ", plus_grand)
# print("nombre de petite ventes : ", tiny_vente)
# print("Le chiffre d'affaire de la journée est : ", total)


# temps_livraisons = [15, 45, -10, 0, 120, 25, 8, -5, 80]
# total_temps = 0
# express = 0
# retard = temps_livraisons[0]

# for temps in temps_livraisons:
#     if temps > 0:
#         total_temps = total_temps + temps

#         if temps < 30:
#             express = express + 1
#         if temps > retard:
#             retard = temps

# print(retard)
# print(express)
# print(total_temps)


# ages_clients = [25, 14, -2, 42, 17, 0, 65, 8, -10]
# mineur = 0
# ca = 0
# billet_majeur = 12
# billet_mineur = 7
# majeur = 0
# total = 0

# for age in ages_clients:
#     if age > 0:
#         if age >= 18:
#             majeur = majeur + 1
#         if age < 18:
#             mineur = mineur + 1
# ca = (mineur * billet_mineur) + (majeur * billet_majeur)


# print(majeur)
# print(mineur)
# print(ca)
