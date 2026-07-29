# Exercice 3.11 : Le générateur de salutations personnalisées
# Crée une fonction "formater_nom" qui prend un prénom et un nom (deux paramètres sous forme de texte).
# Elle doit retourner une seule chaîne de caractères propre : "NOM, Prénom" (avec le nom en majuscules).
# Exemple : formater_nom("alice", "dupont") doit retourner "DUPONT, Alice".


def formater_nom(prenom, nom):
    identity = f"{prenom}, {nom}"
    return identity


print(formater_nom("anis".capitalize(), "ghedabnia".upper()))
