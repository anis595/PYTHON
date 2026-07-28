# Exercice 3.10 : Filtrer les notes au-dessus de la moyenne
# Crée une fonction "filtrer_bonnes_notes" qui prend une liste de notes en paramètre.
# Elle doit parcourir cette liste, garder uniquement les notes supérieures ou égales à 10,
# les stocker dans une nouvelle liste, et retourner cette nouvelle liste.


def filtrer_bonnes_note(liste):

    for note in liste:
        if note >= 10:
            print()
