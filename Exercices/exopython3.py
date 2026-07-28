# Exercice 1.1 : Le téléchargement
# Fais un script qui simule une jauge de téléchargement. Elle part de 0, augmente de 25 en 25, et s'arrête quand elle atteint 100.
# Le programme doit afficher l'évolution de la jauge à chaque étape.

jauge_telechargement = 0
compteur = 0
jauge = 25

while jauge_telechargement < 100:
    jauge_telechargement = jauge_telechargement + jauge
    compteur += 1
    print(compteur, jauge_telechargement)
