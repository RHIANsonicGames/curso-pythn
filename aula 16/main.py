class dragao:
    def __init__(self,nome,elemento,genero,altura, personalidade, aparencia):
        self.nome=nome
        self.elemento=elemento
        self.genero=genero
        self.altura=altura
        self.personalidade=personalidade
        self.aparencia=aparencia

    def apresentar(self):
        print(f"sou {self.nome}, um dragão {self.genero}, eu sou do elemento {self.elemento}, e tenho {self.altura} de altura.")


Hyo= dragao( "Hyo", "Gelo", "femea", "7.9", "feroz, selvagem", "cabelo branco com mechas azuis, olhos cor de cristal, cabelo longo, pele clara, kimono, asas e calda")
Hyo.apresentar()

class Heroi(dragao):
    def __int__(self, nome, elemento, genero, altura):
        super().__int__(nome, elemento, altura)
        self.genero=genero

    def apresentar_heroi(self):
        print(f"meu nome é {self.nome}, eu uso o elemento {self.elemento} e sou do genero {self.genero}. Tenho {self.altura} de altura")


Victor = Heroi("Victor", "fogo", "masculino", "1.76")
Victor.apresentar_heroi()

class Vilao(dragao):
    def __int__(self, nome, elemento, genero, altura):
        super().__int__(nome, elemento, altura)
        self.genero=genero

    def apresentar_vilao(self):
        print (f"meu nome é {self.nome}, uso o elemento {self.elemento}, sou uma {self.genero}. Tenho {self.altura} de altura")


Victoria = Vilao("Victoria", "ar", "garota", "1.60")
Victoria.apresentar_vilao()

