# ==========================================
# Le Défi : Le Validateur de Mot de Passe
# ==========================================

# Mission :
# Crée une fonction nommée "verifier_mot_de_passe" qui prend un seul paramètre :
# 1. mdp : une chaîne de caractères (le mot de passe).

# Ce que doit faire la fonction :
# 1. Si le mot de passe fait moins de 8 caractères, elle doit retourner :
#    "Refusé : trop court"
# 2. Si le mot de passe fait 8 caractères ou plus, MAIS ne contient pas le caractère "@",
#    elle doit retourner : "Refusé : il manque l'arobase"
# 3. Si le mot de passe fait 8 caractères ou plus ET contient bien un "@",
#    elle doit retourner : "Mot de passe valide"


# --- ÉCRIS TA FONCTION ICI ---


def verifier_mot_de_passe(mdp):
    if len(mdp) < 8:
        return f"refusé trop court !"
    if len(mdp) >= 8 and "@" not in mdp:
        return f"refusé il manque le @ !"

    if len(mdp) >= 8 and "@" in mdp:
        return f"Mot de passe valide !"


print(verifier_mot_de_passe("monmotdepasse"))


# --- ZONE DE TESTS ---
# Lance ces prints pour vérifier ton code :

# Test 1 (doit afficher "Refusé : trop court")
# print(verifier_mot_de_passe("loup"))

# Test 2 (doit afficher "Refusé : il manque l'arobase")
# print(verifier_mot_de_passe("monmotdepasse"))

# Test 3 (doit afficher "Mot de passe valide")
# print(verifier_mot_de_passe("monmotdepasse@123"))
