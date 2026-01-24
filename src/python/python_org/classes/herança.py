class Mapeamento:
    def __init__(self, iterável):
        self.lista_itens = []
        self.__atualizar(iterável)

    def atualizar(self, iterável):
        for item in iterável:
            self.lista_itens.append(item)

    __atualizar = atualizar   # cópia privada do método atualizar() original

class SubclasseMapeamento(Mapeamento):

    def update(self, chaves, valores):
        # fornece nova assinatura para atualizar(),
        # mas não quebra __init__()
        for item in zip(chaves, valores):
            self.lista_itens.append(item)


print("Teste da classe Mapeamento:")
m = Mapeamento([1, 2, 3])
print(m.lista_itens)
print()
print("Teste da classe SubclasseMapeamento:")
sm = SubclasseMapeamento([4, 5, 6])
print(sm.lista_itens)
