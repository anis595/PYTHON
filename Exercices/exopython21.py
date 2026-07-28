# Exercice 3.9 : La moyenne d'une liste
# Crée une fonction "calculer_moyenne" qui prend une liste de nombres en paramètre.
# Elle doit calculer la moyenne de ces nombres et retourner le résultat.
# (Indice : tu peux utiliser sum() et len() ou coder une boucle à l'intérieur).


def calculer_moyenne(ma_liste):
    resultat = sum(ma_liste) / len(ma_liste)
    return resultat


print(calculer_moyenne([23, 21, 89, 34]))
