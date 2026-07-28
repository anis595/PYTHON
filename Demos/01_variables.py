import _frozen_importlib

print("Hello, World!")

print(
    """test
        test
            test
"""
)
print(1, "test", 1.9)

ma_variable = 8
print(ma_variable + 5)

var = 23
print(type(var))
var = 2.3
print(type(var))
var = "text"
print(type(var))
var = True
print(type(var))

test_maj = "test".upper()  # .upper() met en majuscule
print(test_maj)
print(test_maj.lower())  # .lower() met en minuscule

ma_recuperation = input(
    "Veuillez entrer votre nom : "
)  # .input() permet de récupérer une informationd
print("Bonjour", ma_recuperation)
print(f"Bonjour {ma_recuperation} , comment allez-vous ?")  # f-string

valeur_a = input("veuillez saisir une valeur A : ")
valeur_b = input("veuillez saisir une valeur B : ")
print(f"vous avez saisi comme valeur A : {valeur_a} et comme valeur B : {valeur_b} ")

nb_a = int(
    input("veuillez saisir un nombre a : ")
)  # int() permet de convertir une variable en entier
nb_b = int(input("veuillez saisir un nombre b : "))

print(nb_a + nb_b)
