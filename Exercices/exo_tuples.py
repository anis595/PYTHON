def recuperer_chiffre(nombre, nombres):
    return (nombre + nombres, nombre - nombres, nombre / nombres, nombre * nombres)


nombre = int(input("donner une valeur "))
nombres = int(input("donner une valeur "))

print(input(recuperer_chiffre(nombre, nombres)))


def operations(nombre1, nombre2):
    addition = nombre1 + nombre2
    soustraction = nombre1 - nombre2
    multiplication = nombre1 * nombre2
    division = nombre1 / nombre2
    return addition, soustraction, multiplication, division


nb1 = int(input("Veuillez saisir un nombre : "))
nb2 = int(input("Veuillez saisir un nombre : "))

# unpack
add, sub, mul, div = operations(nb1, nb2)

print(f"Addition : {add}")
print(f"Soustraction : {sub}")
print(f"Multiplication : {mul}")
print(f"Division : {div}")
