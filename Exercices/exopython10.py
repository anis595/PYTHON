# ==========================================
# Exercice 2.3 : Le calcul du chiffre d'affaires total
# ==========================================
# À partir de la liste de prix : ventes = [120, 45, 300, 85, 210]
# Écris un script avec une boucle for qui additionne tous ces montants
# pour calculer et afficher le chiffre d'affaires total à la fin.


ventes = [120, 45, 300, 85, 210]
compteur = 0

for vente in ventes:
    compteur += vente
print(compteur)
