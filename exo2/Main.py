from classes.CompteBancaire import CompteBancaire

compte = CompteBancaire(51454154, "compte 10", 100)

compte.retrait(-50)
compte.retrait(-100)

compte.versement(150)
