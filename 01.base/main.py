from classes.Chien import Chien

rex = Chien("REX", "berger allemand", 10)
toto = Chien("toto", "berger suisse", 15)


print(rex.nom)

toto.aboyer()
rex.aboyer()

toto.aboyer_sur(rex)
rex.aboyer_sur(toto)

rex.nom = "REX"
print(rex.nom)
