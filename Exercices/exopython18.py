# Exercice 3.6 : Le plus grand des deux
# Crée une fonction "maximum" qui prend DEUX nombres en paramètres (a et b).
# Elle doit retourner le plus grand des deux.


def maximum(nb_a, nb_b):
    if nb_a > nb_b:
        return nb_a
    else:
        return nb_b


print(maximum(600, 200))
