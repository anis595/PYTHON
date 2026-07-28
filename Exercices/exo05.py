# nb_photocopies = int(input("quel est le nombre de photocopie? "))

# if nb_photocopies < 0:
#     print("le nombre de photocopie ne peut pas etre negatif")
# elif nb_photocopies < 10:
#     print(nb_photocopies * 0.5)
# elif nb_photocopies >= 10 and nb_photocopies <= 20:
#     print(nb_photocopies * 0.4)
# else:
#     print(nb_photocopies * 0.3)


# # age = int(input("quel est votre age?"))

# if age (>= 3 ) and (< 6:
#     print("vous êtes Baby")
# elif age >= 7 < 8:
#     print("vous êtes poussin")
# elif age >= 9 < 10:
#     print("vous êtes pupilles")
# elif age >= 11 < 12:
#     print("vous êtes minimes")
# elif age >= 13:
#     print("vous êtes cadet")
# else:
#     print("vous n'etes pas en age de faire du judo")

# temp = int(input("quel est la temperature? "))

# if temp < 0:
#     print("solide")
# elif temp < 100:
#     print("liquide")
# else:
#     print("gazeux")


age = int(input("quel est votre age ? "))


if age >= 30:
    salaire = float(input("quel est votre salire ? "))
    if salaire <= 40000:
        nb_annee = int(input("année d'expérience ? "))
        if nb_annee >= 5:
            print("ok")
        else:
            print("trop peu experimente")
    else:
        print("trop")
else:
    print("trop jeune")
