# ==========================================
# Exercice 2.4 : La recherche de la note maximale
# ==========================================
# À partir de la liste de notes : notes = [12, 8, 19, 14, 16]
# Écris un script avec une boucle for qui parcourt la liste et trouve
# quelle est la note la plus haute, puis l'affiche à la fin.


notes = [12, 8, 19, 14, 16]
max_note = notes[0]

for note in notes:
    if note > max_note:
        max_note = note

print(max_note)
