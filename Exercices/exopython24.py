# ==========================================
# Le Défi : La Caisse Automatique
# ==========================================

# Mission :
# Crée une fonction nommée "caisse_automatique" qui accepte très exactement deux paramètres :
# 1. panier : une liste contenant des prix (des nombres).
# 2. carte_vip : un booléen (True ou False).

# Ce que doit faire la fonction :
# 1. Calculer la somme totale des prix présents dans le panier.
# 2. Si le client possède la carte VIP (True), appliquer une réduction de 20 % sur le total.
# 3. Retourner une seule chaîne de caractères formatée exactement comme ceci :
#    "Total à payer : X euros." (où X est le montant final calculé).


# --- ÉCRIS TA FONCTION ICI ---


def caisse_automatique(panier, carte_vip):
    if carte_vip == True:
        total = sum(panier)
        reduction = total * 0.2
        final = total - reduction
        return f" Total à payer :{final}"
    if carte_vip == False:
        total = sum(panier)
        return f" Total à payer :{total}"


print(caisse_automatique([10, 20, 50], False))
