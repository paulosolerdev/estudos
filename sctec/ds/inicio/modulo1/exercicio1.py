# 1. Crie uma lista e use a declaração da lista;
lista = [1, 2, 3, 4, 5]

# 2. Depois aplique os princípios de pilha, filha e lista que aprendemos
# nesta aula, adicionando e inserindo frutas.

# Pilha
pilha = []
pilha.append('Maçã')
pilha.append('Banana')
pilha.append('Laranja')
print("Pilha:", pilha)
pilha.pop()
print("Pilha após pop:", pilha)

print("$==============================================$")

# Fila
from collections import deque
fila = deque()
fila.append('Maçã')
fila.append('Banana')
fila.append('Laranja')
print("Fila:", fila)
fila.popleft()
print("Fila após popleft:", fila)

print("$==============================================$")
# Lista
lista_de_frutas = ['Maçã', 'Banana', 'Laranja']
print("Lista de frutas:", lista_de_frutas)
lista_de_frutas.append('Uva')
print("Lista de frutas após adicionar Uva:", lista_de_frutas)
lista_de_frutas.remove('Banana')
print("Lista de frutas após remover Banana:", lista_de_frutas)

print("$==============================================$")


# 3. Utilize o laço de repetição para imprimir todos elementos dessa lista;
print("Imprimindo elementos da lista de frutas:")
for fruta in lista_de_frutas:
    print(fruta)

# 4. E por fim, crie uma condição para imprimir somente a maçã e laranja. 
# Você só pode imprimir a maçã e laranja.
print("Imprimindo somente a maçã e laranja:")
for fruta in lista_de_frutas:
    if fruta == 'Maçã' or fruta == 'Laranja':
        print(fruta)
