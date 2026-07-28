increment = 0

while increment < 10:
    increment += 1
    if increment == 3:
        continue  # on continue la boucle
    if increment == 7:
        break  # on arrête la boucle
    print(increment)


for i in range(0, 11):  # on part de 0 et on s'arrete a 10
    print(i)


for i in range(0, 11, 2):  # on part de 0 et on s'arrete a 10 avec un pas de 2
    print(i)


for i in range(300, 200, -1):
    print(i)
