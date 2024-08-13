#Declarando lista de herois iniciais
def Personagens():

 herois = [
  {"nome": "Berely", "title": "earth punch", "elemento": "eletricidade", "poder": 110},
  {"nome": "Seraph", "title": "fire god", "elemento": "fogo", "poder": 90},
  {"nome": "Bella", "title": "wind mas-ter", "elemento": "ar", "poder": 35},
  {"nome": "Mei", "title": "tsunami", "elemento": "água", "poder": 64}
 ]

 #Declarando lista de dragoes iniciais
 dragoes = [
  {"nome": "Teros", "title": "destroyer of worlds", "elemento": "fogo", "poder": 180},
  {"nome": "Kingice", "title": "the ice lord", "elemento": "gelo", "poder": 120},
  {"nome": "Strong", "title": "Tornado the wind controller", "elemento": "ar", "poder": 97},
  {"nome": "leviata", "title": "the water itself", "elemento": "água", "poder": 115}
 ]

 #Recebe dados do usuario
 print("crie seu personagem")








 time = float(input("escolha seu time (1=herois, 2=dragoes) :"))
 while time != 1 and time != 2:
     time = float(input("escolha seu time (1=herois, 2=dragoes) :"))
     if time != 1 and time != 2:
      print("time incorreto")





 print(f"você é do time {time}")
 print("")

 nome = input("escolha seu nome :")
 print(f"seu nome é {nome}, que nome lindo :")

 print("")

 title = input("crie um apelido/titulo :")
 print(f"{title}, belo apelido")

 print("")

 elemento = input("crie ou escolha um elemento :")
 print(f"seu elemento é {elemento}")

 print("")

 #Usuario digita sua forca limitado a 1000
 poder = int(input("qual o seu power level/força total? (maximo 100) :"))

 while poder > 100:
     poder = int(input("qual o seu poder/força total? (maximo 100) :"))

 print("")

 print(f"esses são seus dados:")

 print("")

 print(f"Nome = {nome}")
 print(f"titulo = {title}")
 print(f"Time = {time}")
 print(f"Elemento = {elemento}")
 print(f"força total = {poder}")

 print("")

 print("seus dados selecionados são: 1-nome: "+nome+"/ 2-elemento: ",elemento+"/ 3-titulo ",title,"/ 4-poder: "+poder)

 novo_personagem = {"nome": nome, "elemento": elemento, "poder": poder, "title": title}

 if time == "1":
  herois.append(novo_personagem)
  print("HEROIS ATUALIZADOS")
  print(herois)
 else:
  dragoes.append(novo_personagem)
  print("DRAGOES ATUALIZADOS")
  print(dragoes)