"""
Exercício Análise de Números Inteiros e Reais

Objetivo: Desenvolver um programa que obtenha do usuário dois números
inteiros e um número real, e em seguida realize e apresente uma série
de cálculos e análises relacionadas a esses números.

Instruções:

1. Solicite ao usuário dois números inteiros.
2. Solicite ao usuário um número real.
3. Calcule e exiba o produto do dobro do primeiro número com metade do segundo número.
4. Calcule e exiba a soma do triplo do primeiro número com o terceiro
número.
5. Calcule e exiba o terceiro número elevado ao cubo.
6. Determine e informe se o primeiro número é par ou ímpar.
7. Determine e informe se o terceiro número é positivo, negativo ou zero.
8. Calcule e mostre a média aritmética dos três números.

"""


# Função principal do programa
def main():
    # Solicita ao usuário dois números inteiros
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    # Solicita ao usuário um número real
    num3 = float(input("Digite um número real: "))

    # Cálculo do produto do dobro do primeiro número com metade do segundo número
    produto = (2 * num1) * (num2 / 2)
    print(
        f"Produto do dobro do primeiro número com metade do segundo número: {produto}"
    )

    # Cálculo da soma do triplo do primeiro número com o terceiro número
    soma = (3 * num1) + num3
    print(f"Soma do triplo do primeiro número com o terceiro número: {soma}")

    # Cálculo do terceiro número elevado ao cubo
    cubo = num3**3
    print(f"Terceiro número elevado ao cubo: {cubo}")

    # Determinação se o primeiro número é par ou ímpar
    if num1 % 2 == 0:
        print(f"O primeiro número ({num1}) é par.")
    else:
        print(f"O primeiro número ({num1}) é ímpar.")

    # Determinação se o terceiro número é positivo, negativo ou zero
    if num3 > 0:
        print(f"O terceiro número ({num3}) é positivo.")
    elif num3 < 0:
        print(f"O terceiro número ({num3}) é negativo.")
    else:
        print(f"O terceiro número ({num3}) é zero.")

    # Cálculo da média aritmética dos três números
    media = (num1 + num2 + num3) / 3
    print(f"Média aritmética dos três números: {media}")


if __name__ == "__main__":
    main()
