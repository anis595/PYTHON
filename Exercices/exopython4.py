# Exercice 1.2 : Le vigile intransigeant
# Fais un script qui demande à l'utilisateur de taper un mot.
# Tant qu'il ne tape pas exactement "OUI", le programme le bloque, lui dit "Non, essayez encore" et lui redemande.
# S'il tape "OUI", le programme se termine en affichant "Vous pouvez passer !".


mot = input("Veuillez taper un mot : ")

while mot != "oui":
    print("Non, essayez encore")
    mot = input("Veuillez taper un mot : ")
    print("Vous pouvez passer !")
