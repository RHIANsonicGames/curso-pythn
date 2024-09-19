

class Personagem:
    def __init__(self, nome, elemento, cor):
        self.nome = nome
        self.elemento = elemento
        self.cor = cor


def apresentar():
    print(f"sou {self.nome} do elemento {self.elemento} e cor {self.cor}")


class Dragao (Personagem):
    def __init__(self, nome, elemento, cor, forca):
        super().__init__(nome, elemento, cor)
        self: forca = forca

    def apresentar():
        print(f"sou {self.nome} do elemento {self.elemento} e cor {self.cor}")

class heroi(Personagem):
    def __init__(self, nome, elemento, cor, forca):
        super().__init__(nome, elemento, cor)
        self.forca = forca


Dragalo = Dragao("Dragalo", "fogo", "Amarelo", 87)
Dragalo.apresentar()


Zawarudo = heroi("zawarudo", "time", "dourado", 90)
Zawarudo.apresentar()


class Heroi(Dragao):
    def __init__(self, nome, elemento, cor, habilidade):
        super().__init__(nome, elemento, cor)
        self.habilidade = habilidade
def apresentar_heroi(self):
    print(f"Sou {self.nome}, um herói do elemento {self.elemento}.Minha habilidade especial é {self.habilidade}.")
