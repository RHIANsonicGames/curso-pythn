

itens = ["esmeralda", "diamante", "ouro", "ametista", "obsidiana"]

select = input("Olá! temos esmeralda, diamante, ouro, ametista e obsidiana, o que desejas?")

existe = False

for item in itens:

    if item == select:
        print(item)
        print(f"existe nesse estoque o produto {select}")
        existe = True
        break

if existe == False:
    print(f"não temos o produto {select}")

