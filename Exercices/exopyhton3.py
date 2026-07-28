ventes = [120, 50, -10, 300, 0, 45, -5]
ventes_valides = []

for i in ventes:
    if i > 0:
        ventes_valides.append(i)
total = sum(ventes_valides)
print(ventes_valides, total)
