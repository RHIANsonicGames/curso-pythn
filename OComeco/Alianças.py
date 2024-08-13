def aliancas_magicas = []
for heroi in herois:
   for dragao in dragoes:
      if heroi["elemento"] == dragao["elemento"]:
       aliancas_magicas.append((heroi["nome"], dragao["nome"]))




    print("Alianças Mágicas Formadas:")
    print(f"{aliancas_magicas[0]} e {aliancas_magicas[1]}")

