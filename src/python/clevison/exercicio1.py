"""
Exercício Análise de Números

Objetivo: Desenvolver um programa que solicita ao usuário a entrada de um 
número e, com base nesse número, realiza as seguintes operações:

1. Mostrar o número informado.
2. Informar se o número é par ou ímpar.
3. Informar se o número é positivo, negativo ou zero.
4. Se o número for positivo, calcular e mostrar sua raiz quadrada.

"""

import math


def analisar_numero():
    numero = float(input("Digite um número: "))
    
    print(f"Número informado: {numero}")
    
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    
    if numero > 0:
        print("O número é positivo.")
        raiz_quadrada = math.sqrt(numero)
        print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")


if __name__ == "__main__":
    analisar_numero()
