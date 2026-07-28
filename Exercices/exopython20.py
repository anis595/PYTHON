# Exercice 3.8 : Le premier élément
# Crée une fonction "premier_element" qui prend une liste en paramètre
# et retourne uniquement le premier élément de cette liste.


def premier_element(ma_liste):
    for i in ma_liste:
        return i


print(premier_element(["chat", "chien"]))
