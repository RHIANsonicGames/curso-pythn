from soma import somar
from divisão import dividir
from multiplicação import multiplicar
from subtração import subtrair

continua= 1
while continua== 1:

    print("escolha uma operacao")
    operacao= float(input("1-soma/ 2-divisao/ 3-multiplicacao/ 4-subtracao:"))

    numero= float(input("por favor, digite o valor 1:"))
    numero2= float(input("por favor, digite o valor 2:"))

    if operacao==1:
        rest= somar(numero, numero2)
    if operacao==2:
        rest= dividir(numero, numero2)
    if operacao==3:
        rest= multiplicar(numero, numero2)
    if operacao==4:
        rest= subtrair(numero, numero2)

    print(f"O resultado de sua operação foi {rest}")
    continua = int(input("deseja continuar? 1=sim/ 2=nao:"))