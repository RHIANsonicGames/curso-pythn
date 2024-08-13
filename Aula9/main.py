regras= ["ter frequencia", "respeitar o próximo", "cuidar dos equipamentos", "fazer os exercicios", "zelo com o ambiente", "não jogar durante a aula"]
regras.append("Ajudar quem tem dificuldade")
regras.remove("ter frequencia")
quantidade= len(regras)
cont= 0
while cont < quantidade:
    print(regras [cont])
    cont= cont+1
if "respeitar o próximo" in regras:
    print("respeitar o próximo, regra concluida!")
else:
    print("respeitar o próximo, regra em falta!")