import json

path_file = r"./Demos/personne.json"

with open(path_file, "r", encoding="UTF-8") as file:
    personnes = json.load(file)
    print(personnes)
    print(type(personnes))
    print(personnes[1]["age"])

personnes.append({"prenom": "toti", "age": 30, "email": "toto@email.com"})
print(personnes)

with open(path_file, "w", encoding="UTF-8") as file:
    json.dump(personnes, file, indent=4)
