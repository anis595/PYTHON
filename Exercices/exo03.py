import math

rayon = float(input("veuillez saisir le rayon: "))
hauteur = float(input("veuillez saisir la hauteur: "))

volume = math.pi * rayon**2 * hauteur // 3
print(f"le volume est : {volume}")
