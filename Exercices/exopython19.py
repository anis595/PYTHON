# Exercice 3.7 : La vérification de stock
# Crée une fonction "verifier_stock" qui prend le stock actuel (un nombre)
# et un seuil minimum requis.
# Elle doit retourner True si le stock est supérieur ou égal au seuil, et False sinon.


def verifier_stock(nb):
    if nb > 10:
        return True
    else:
        return False


print(verifier_stock(100))
