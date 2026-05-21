class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e tenho {self.altura} de altura.')


p1 = Pessoa('João', 30, "1,75")
p2 = Pessoa('Karina', 25, "1,65")

p1.apresentar()
p2.apresentar()
