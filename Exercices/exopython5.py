# Exercice 1.3 : Le Juste Prix
# Le nombre secret à deviner est 73.
# Fais un script qui demande à l'utilisateur de deviner le nombre.

# Si la proposition est trop petite, le programme affiche "C'est plus !".

# Si c'est trop grand, il affiche "C'est moins !".

# Le programme doit continuer de demander tant que le joueur n'a pas trouvé le bon nombre.

# Quand il trouve, la boucle s'arrête et le programme affiche "Gagné !".


nb = int(input("Devine le nombre ! "))


while nb != 73:
    if nb < 73:
        print("c'est plus !")

    elif nb > 73:
        print("c'est moins! ")
    nb = int(input("retente ta chance !"))

print("C'est gagné !")
