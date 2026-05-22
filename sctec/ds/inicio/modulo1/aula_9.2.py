"""

Codifique em python um contador de números pares

1. Utilize o laço de repetição 'for' para contar ou iterar entre um
intervalo de números e imprimir no terminal todos os números pares
dentro desse intervalo de números.

2. Escreva um programa que solicita ao usuário dois números: o início
e o fim de um intervalo (inclusivos).

3. O programa deve imprimir todos os números pares dentro desse intervalo.

O resultado desse código, seria apresentar no terminal os números pares
entre 1 e 10, que seriam: 2, 4, 6, 8 e 10.

"""

# 1.
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)
    
# 2.
inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

# 3.
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        print(numero)
