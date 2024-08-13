
from Lista_De_Personagens import Personagens

Personagens()
















#Recebe dados do usuario
print("crie seu personagem")

time = input("escolha seu time (1=dragoes, 2=herois)")
print(f"você é do time {time}")

print("")

nome = input("escolha seu nome")
print(f"seu nome é {nome}, que nome lindo")

print("")

elemento = input("crie ou escolha um elemento")
print(f"seu elemento é {elemento}")

print("")

#Usuario digita sua forca limitado a 1000
power_Level = float(input("qual o seu power level/força total?"))

while power_Level > 1000:
    power_Level = float(input("qual o seu power level/força total?"))


print("")

print(f"esses são seus dados:")

print("")

print(f"Nome = {nome}")
print(f"Time = {time}")
print(f"Elemento = {elemento}")
print(f"força total = {power_Level}")




