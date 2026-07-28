# ==========================================
# Exercice 2.5 : Le filtre de catégorie (Le boss des boucles for)
# ==========================================
# À partir de la liste de mots : mots = ["chat", "ordinateur", "python", "riz", "data"]
# Écris un script avec une boucle for et un if qui parcourt cette liste
# et affiche UNIQUEMENT les mots qui contiennent plus de 4 lettres.
# (Indice : cherche comment compter la longueur d'une chaîne de caractères en Python).

mots = ["chat", "ordinateur", "python", "riz", "data"]


for mot in mots:
    if len(mot) > 4:
        print(mot)
