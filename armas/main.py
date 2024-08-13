print("você nasceu com os poderes de criar armas")
print("")

print("bandidos invadiram sua casa, escolha os itens para você se defender:")
armas=["faca", "travesseiro", "colher", "garfo", "madeira"]

for indice , item in enumerate(armas):
    print(f"{indice}-{item}")
quantidade=len(armas)
print(quantidade)
v=""
while v != "x":
    item_criado=input("escolha um nome para seu item criado")
    v=item_criado
    if v != "x":
        armas.append(item_criado)

print(f"armas que você possui: {armas} ")
remova_arma=input("quer remover alguma arma?")
armas.remove(remova_arma)

