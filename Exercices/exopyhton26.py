# ==========================================
# Le Défi : Le Contrôleur de Drone FPV
# ==========================================

# Contexte :
# Tu codes le système d'un drone. Il reçoit ses instructions de vol sous
# forme de chaîne de caractères.
# Les seules commandes autorisées sont :
# 'A' (Avancer), 'S' (Stationnaire), 'P' (Photo), 'F' (Flip acrobatique).

# 1. Écrire une fonction "verification_vol(sequence)" qui renvoie True si
#    la séquence de vol est valide (composée uniquement de A, S, P, F),
#    et False si elle est invalide. (Gère majuscules et minuscules).

# 2. Écrire une fonction "saisie_vol()" qui demande à l'utilisateur de saisir
#    une séquence, vérifie sa validité, et boucle tant que la saisie est fausse.
#    Elle renverra la séquence valide sous forme de chaîne (tout en majuscules).

# 3. Écrire une fonction "analyse_combo(sequence, combo)" qui reçoit deux
#    paramètres (la séquence complète, et un combo précis, ex: "AF" pour Avancer+Flip).
#    Elle renverra le nombre de fois où ce combo a été réussi dans la séquence.

# 4. [Le Bonus Costaud] Écrire une fonction "rapport_telemetrie(sequence)" qui
#    calcule l'état final du drone après son vol.
#    Règles :
#    - Le drone démarre avec 100% de batterie et 0 photo dans la mémoire.
#    - 'A' consomme 2% de batterie.
#    - 'F' consomme 5% de batterie.
#    - 'S' consomme 1% de batterie.
#    - 'P' prend 1 photo (0% de batterie consommée).
#    - ATTENTION : Si la batterie tombe à 0% ou moins pendant la lecture de
#      la séquence, le drone s'écrase. Le calcul s'arrête immédiatement et la
#      fonction doit retourner : "CRASH : Batterie épuisée."
#    - Si le vol se termine sans crash, retourner une phrase formatée :
#      "Atterrissage réussi. Batterie: X%, Photos: Y"

# 5. Créer les instructions (des prints) tout en bas pour pouvoir tester
#    les différentes fonctions de ton programme.


# --- ÉCRIS TON CODE EN DESSOUS ---


def verification_vol(sequence):
    if sequence == "A,S,P,F":
        return True
    else:
        return False


def saisie_vol(saisi):

    while saisi != "A,S,P,F":
        print("sequence erronée")
        saisi = input("veuillez entrer la séquence : ")
    if saisi == "A,S,P,F":
        print("ok")
        return True


saisie = input("veuillez entrer la séquence requise : ")
saisie_vol(saisie)


def analyse_combo(sequence, combo):
    print
