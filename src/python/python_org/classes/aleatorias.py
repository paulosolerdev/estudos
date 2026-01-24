# class Armazem:
#     proposito = 'armazenar'
#     regiao = 'oeste'


# a1 = Armazem()
# print(a1.proposito, a1.regiao)

# a2 = Armazem()
# a2.regiao = 'leste'
# print(a2.proposito, a2.regiao)


#==============================================#


class Bolsa:
    def __init__(self):
        self.data = []

    def adicionar(self, x):
        self.data.append(x)

    def adicionar_em_dobro(self, x):
        self.adicionar(x)
        self.adicionar(x)

