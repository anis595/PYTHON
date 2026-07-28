depart = 2000
annee = 0
t = int(input("entré le taux: ")) / 100

while depart < 3000:
    annee += 1
    depart = depart * (1 + t)
print(f"Il a fallu {annee} ans pour cumuler{int(depart)}€")
