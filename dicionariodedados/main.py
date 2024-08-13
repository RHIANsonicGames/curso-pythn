herois = [
 {"nome": "Berely", "title": "earth punch", "elemento": "eletricidade", "poder": 110},
 {"nome": "Seraph", "title": "fire god", "elemento": "fogo", "poder": 90},
 {"nome": "Bella", "title": "wind master", "elemento": "ar", "poder": 35},
 {"nome": "Mei", "title": "tsunami", "elemento": "água", "poder": 64}
]


dragoes = [
 {"nome": "Teros", "title": "destroyer of worlds", "elemento": "fogo", "poder": 180},
 {"nome": "Kingice", "title": "the ice lord", "elemento": "gelo", "poder": 120},
 {"nome": "Strong", "title": "Tornado the wind controller", "elemento": "ar", "poder": 97},
 {"nome": "Kilimbari", "title": "the water itself", "elemento": "água", "poder": 115}
]

aliancas_magicas = []
for heroi in herois:
   for dragao in dragoes:
      if heroi["elemento"] == dragao["elemento"]:
       aliancas_magicas.append((heroi["nome"], dragao["nome"]))




print("Alianças Mágicas Formadas:")
print(f"{aliancas_magicas[0]} e {aliancas_magicas[1]}")
