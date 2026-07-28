# ==========================================
# Exercice 2.2 : Le filtre d'âge
# ==========================================
# À partir de la liste ages = [15, 22, 9, 34, 18],
# écris un script qui compte combien de personnes sont majeures (18 ans et plus).
# Le programme doit uniquement afficher le nombre total à la toute fin.


liste_ages = [15, 22, 9, 34, 18]
compteur = 0

for age in liste_ages:
    if age >= 18:
        compteur += 1

print(compteur)
