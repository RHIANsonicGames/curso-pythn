nome = input("digite seu nome:")
idade = input("digite sua idade:")
dia = input("como vai seu dia?:")
esporte = input("qual seu esporte favorito?:")
jogo = input("qual seu jogo favorito?:")
cor = input("qual sua cor favorita?:")
comida = input("qual sua comida favorita?:")

print(f"bom dia {nome}, voce tem {idade} anos e seu esporte favorito é {esporte}, e voce gosta de jogar {jogo}, fique sabendo que eu tambem gosto, sua cor favorita é {cor}, eu tambem gosto de {cor}, e sua comida favorita é {comida}, você tem bons gostos, ")
print("ㅤ")
numero1= float(input("digite o priemiro numero:"))
numero2 = float(input("digite o segundo numero:"))
operacao = input("escolha a operação(+,-,*,/):")

if operacao =='+':
    resultado = numero1 + numero2
elif operacao =='-':
    resultado = numero1 - numero2
elif operacao =='*':
    resultado = numero1 * numero2
elif operacao =='/':
    resultado = numero1/numero2
else:
    resultado = "Operação inválida"

print (f"O resultado da sua operação é: {resultado}")+