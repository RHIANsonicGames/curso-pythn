continua= 1
while continua== 1:

    print("escolha uma operacao")
    operacao= float(input("1-soma/ 2-divisao/ 3-multiplicacao/ 4-subtracao:"))

    numero= float(input("por favor, digite o valor 1:"))
    numero2= float(input("por favor, digite o valor 2:"))


    if operacao==1:
        rest= numero+ numero2
    if operacao==2:
        rest= numero/ numero2
    if operacao==3:
        rest= numero* numero2
    if operacao==4:
        rest= numero- numero2

    print(rest)
    continua = int(input("deseja continuar? 1=sim/ 2=nao:"))

