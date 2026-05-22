# class Pessoa:
#     def __init__(self, nome, idade, altura):
#         self.nome = nome
#         self.idade = idade
#         self.altura = altura

#     def apresentar(self):
#         print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e tenho {self.altura} de altura.')


# p1 = Pessoa('João', 30, "1,75")
# p2 = Pessoa('Karina', 25, "1,65")

# p1.apresentar()
# p2.apresentar()



#====================================================================#


"""
1. Crie uma classe chamada Carro;

2. Defina seus atributos: modelo, placa e ano;

3. Em seguida, crie os seguintes métodos: mostrarplaca() e ao instanciar
a classe a partir de um objeto, mostre a placa deste veículo.

"""


class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        print(f'Veículo {self.modelo} com placa {self.placa} do ano {self.ano} foi criado.')
    
    def mostrarplaca(self):
        print(f'A placa do veículo é: {self.placa}')

carro1 = Carro('Fusca', 'ABC-1234', 1970)
carro1.mostrarplaca()
