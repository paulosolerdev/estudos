class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.altura = altura

    def apresentar(self):
        print(f'Olá, meu nome é {self.__nome}, tenho {self.__idade} anos e {self.altura} de altura.')

    def get_nome(self):
        return self.__nome
    
    def set_idade(self, nova_idade):
        if nova_idade < 40:
            self.__idade = nova_idade

# p1 = Pessoa('João', 30, "1,75")
# p2 = Pessoa('Karina', 25, "1,65")

# p1.apresentar()
# p2.apresentar()

# p1.set_idade(40)
# p2.apresentar()

# print(p1.get_nome())

#================================================================#

# # Herança

# class Aluno(Pessoa):
#     def __init__(self, nome, idade, altura, matricula):
#         super().__init__(nome, idade, altura)
#         self.matricula = matricula

#     def estudante(self):
#         print(f'A matrícula do aluno é: {self.matricula}')

# aluno1 = Aluno('Maria', 20, "1,60", '2024001')
# aluno1.apresentar()
# aluno1.estudante()

#================================================================#

# Polimorfismo

 class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade, altura)
        self.matricula = matricula

    def estudante(self):
        print(f'A matrícula do aluno é: {self.matricula}')

aluno1 = Aluno('Maria', 20, "1,60", '2024001')
aluno1.apresentar()
aluno1.estudante()
