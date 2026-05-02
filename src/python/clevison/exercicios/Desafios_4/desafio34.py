"""
Exercício Operações Matemáticas Básicas

Objetivo: Desenvolver um programa que solicite ao usuário a entrada de dois
números e, com base nesses números, realize as seguintes operações:

1. Calcular e mostrar a soma dos dois números.

2. Calcular e mostrar a subtração do primeiro número pelo segundo.

3. Calcular s mostrar a multiplicação dos dois números.

4. Calcular e mostrar a divisão do primeiro número pelo segundo (se o segundo
número não for zero).

5. Verificar e informar se algum dos números (ou ambos) é zero.

6. Calcular e mostrar a média dos dois números.

7. Comparar os dois números e informar qual é maior ou se são iguais.

"""

def operacoes_matematicas():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    
    if num2 != 0:
        divisao = num1 / num2
        print(f"Divisão: {divisao}")
    else:
        print("Divisão por zero não é permitida.")
    
    if num1 == 0 or num2 == 0:
        print("Um dos números é zero.")
    
    media = (num1 + num2) / 2
    print(f"Média: {media}")
    
    if num1 > num2:
        print("O primeiro número é maior.")
    elif num2 > num1:
        print("O segundo número é maior.")
    else:
        print("Os dois números são iguais.")


if __name__ == "__main__":
    operacoes_matematicas()
