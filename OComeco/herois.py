def read_heroes(file_path):
heroes = [
 {"nome": "Berely", "title": "earth punch", "elemento": "eletricidade", "poder": 110},
 {"nome": "Seraph", "title": "fire god", "elemento": "fogo", "poder": 90},
 {"nome": "Bella", "title": "wind master", "elemento": "ar", "poder": 35},
 {"nome": "Mei", "title": "tsunami", "elemento": "água", "poder": 64}
]

with open(file_path, "r") as file:
 lines = file.readlines()
 for line in lines:
 name, health, attack = line.strip().split(",")
 hero = Hero(name, int(health), int(attack))
 heroes.append(hero)
 return heroes