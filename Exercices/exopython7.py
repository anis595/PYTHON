# Le bon code PIN est "1234". L'utilisateur n'a le droit qu'à 3 essais maximum.
# Demande le code à l'utilisateur.
# Tant que le code est faux ET qu'il lui reste des essais, le programme lui dit "Code erroné"
# et lui redemande le code.
# Si l'utilisateur trouve le bon code avant d'avoir épuisé ses essais, la boucle s'arrête
# et affiche "Accès autorisé".
# S'il rate ses 3 essais, la boucle s'arrête et le programme affiche "Carte avalée".


code = int(input("Veuillez entrer votre code PIN : "))
essaie = 0

while code != 1234 and essaie < 2:
    print("code érroné")
    essaie += 1
    code = int(input("Veuillez entrer votre code PIN : "))


if code == 1234:
    print("accés autorisé")
else:
    print("carte bloqué")
