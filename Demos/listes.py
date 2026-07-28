# pour instancier une liste on utilise des crochets []
#           0, 1, 2, 3, 4         5            <= INDEX
ma_liste = [1, 2, 3, 4, 5, ["a", "b", "c"]]

# afficher un élément de ma liste
print(ma_liste)
print(ma_liste[2])
print(ma_liste[5][1])

# remplacer une valeur déjà existante
ma_liste[4] = 8
print(ma_liste)
# ma_liste[6] = 'toto' => la liste ne dépasse pas l'index 5 donc erreur

# Pour ajouter un ou plusieurs elements à la fin de ma liste
ma_liste.append(10)
print(ma_liste)

# Pour ajouter à un emplacement donné
ma_liste.insert(0, "premier")
print(ma_liste)

# POur jaouter une liste d'éléments
ma_liste.extend(["d", "e", "f"])
print(ma_liste)

# pour retirer un élément avec l'index et renvoyer l'élément
test = ma_liste.pop(5)
print(test)
print(ma_liste)

# pour retirer un via la valeur (uniquement le premier qui correspond)
ma_liste.remove(1)
print(ma_liste)

ma_liste[4].remove("a")

for element in ma_liste:
    print(element)
