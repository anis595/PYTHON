# Exercice 3.5 : La conversion de devises
# Crée une fonction "convertir_en_dollars" qui prend un montant en euros,
# le multiplie par 1.1 pour le convertir en dollars, et retourne le montant converti.
# Teste-la avec 100 et affiche le résultat.


def convertir_en_dollar(montant):
    resultat = montant * 1.1
    return resultat


print(convertir_en_dollar(100))
