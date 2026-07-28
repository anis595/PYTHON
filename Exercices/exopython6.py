# ==========================================
# Exercice 1.4 : La Caisse Enregistreuse
# ==========================================
# Un client te doit 50 euros.
# Fais un script qui lui demande d'insérer de la monnaie (un input où il tape un montant).
# Tant que le reste à payer est supérieur à zéro, le programme affiche ce qu'il reste à payer
# et redemande d'insérer de la monnaie.
# Si le client a tout payé (ou donné trop d'argent), la boucle s'arrête.
# À la fin, le programme affiche "Paiement accepté", et calcule la monnaie à rendre si le client a donné plus que prévu.


reste_a_payer = 50
compteur = 0

while reste_a_payer > 0:
    compteur += 1
    nb = int(input(" Merci d'insérer la monnaie !"))
    reste_a_payer = reste_a_payer - nb
    print(reste_a_payer)

print("paiment accépté")

if reste_a_payer < 0:
    reste_a_payer = reste_a_payer * (-1)
    print(f"tenez voici votre monnaie ! {reste_a_payer}")
