from dataclasses import dataclass

@dataclass
class Empregado:
    nome: str
    dept: str
    salario: int

joao = Empregado('João', 'lab de computadores', 1000)
print(joao.dept)

print(joao.salario)
