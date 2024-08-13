import random

secret = random.randrange(1,100)
rsecret =0

while rsecret != secret:
    rsecret = float(input("acerte um numero de 1 a 100"))
    if rsecret > secret:
        print("menor")

    elif rsecret < secret:
        print("maior")

    elif rsecret == secret:
        print("você acertou")

