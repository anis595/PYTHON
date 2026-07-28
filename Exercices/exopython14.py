# ==========================================
# Exercice 3.2 : L'usine à ristourne
# ==========================================
# Crée une fonction nommée "appliquer_solde" qui prend un prix en paramètre,
# lui soustrait 10 euros, et retourne le nouveau prix avec return.
# En dehors de la fonction, appelle-la avec un prix de 50,
# et affiche le résultat retourné avec un print.


def appliquer_solde(prix):
    resultat = prix - 10
    return resultat


print(appliquer_solde(50))
