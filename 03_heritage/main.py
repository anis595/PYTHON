from classes.Voiture import Voiture
from classes.Moto import Moto

v1 = Voiture("V1", "rouge", "m1", 5)
m1 = Moto("V1", "rouge", "m1", "sport")

print(v1.demarrer())
print(v1.afficher())
print(m1.afficher())
