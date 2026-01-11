# class MinhaClasse:
#     """Documentação: Um exemplo de classe simples.
#     Esta classe demonstra atributos e métodos básicos em Python.
#     """
#     i = 12345

#     def f(self):
#         return 'Olá, mundo!'
    
# obj = MinhaClasse()

# print(obj.i)

# print(obj.f())

# print(obj.__doc__)


#====================================================#


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
x = Complex(3.0, -4.5)
print(f'{x.r}, {x.i}')
