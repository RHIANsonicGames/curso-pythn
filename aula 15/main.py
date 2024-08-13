class dragao:
    def __init__(self,nome,elemento,genero,altura):
        self.nome=nome
        self.elemento=elemento
        self.genero=genero
        self.altura=altura

    def apresentar(self):
        print(f"sou {self.nome}, um dragão {self.genero}, eu sou do elemento {self.elemento}, e tenho {self.altura} de altura.")


Hyo= dragao( "Hyo", "Gelo", "femea", "7.9")
Hyo.apresentar()

class prota:
    def __init__(self,nome,poderes,genero,altura):
        self.nome=nome
        self.poderes=poderes
        self.genero=genero
        self.altura=altura

    def apresentar(self):
        print(f"sou {self.nome}, uma pessoa que veio parar neste mundo, tenho {self.poderes}, e sou {self.genero}, possuo {self.altura} de altura")

Victor= prota( "Victor", "manipulação de fogo, escudo mítico", "homem", "1.78")
Victor.apresentar()
