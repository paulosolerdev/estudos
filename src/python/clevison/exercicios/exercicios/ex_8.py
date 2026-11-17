"""
Exercício: Análise de Caracteres e Formação de Palavras

Objetivo: Desenvolver um programa que obtenha do usuário uma letra ou uma
palavra e realize análises sobre o tipo de caractere inserido, além de
funções adicionais se uma palavra completa for fornecida.

Instruções:

1. Solicite ao usuário que digite uma letra ou uma palavra.


2. Se o usuário digitar apenas um caractere:

a. Verifique se é uma vogal ou consoante.
b. Se for uma vogal, exiba: "Você digitou uma vogal."
c. Se for uma consoante, exiba: "Você digitou uma consoante."
d. Se o caractere não for uma letra, exiba: "Caractere inválido."


3. Se o usuário digitar uma palavra (mais de um caractere):

a. Calcule e exiba o número de vogais na palavra.
b. Calcule e exiba o número de consoantes na palavra.
c. Exiba a palavra invertida.
d. Informe se a palavra é um palíndromo (lê-se da mesma forma
de trás para frente).


4. Peça ao usuário se deseja verificar outra letra ou palavra ou sair
do programa.


Observações: O programa deve considerar letras maiúsculas e minúsculas
(ou seja, "A" e "a" são ambas vogais).

"""


# Solução do exercício

vogais = ["a", "e", "i", "o", "u"]

while True:
    # 1. Solicitar ao usuário que digite uma letra ou uma palavra.
    entrada_usuario = input("Digite uma letra ou uma palavra: ").lower()

    if len(entrada_usuario) == 1:
        # Converte o caractere inserido para minúsculo
        char = entrada_usuario.lower()

        if char in vogais:
            print("Você digitou uma vogal.")

        elif char.isalpha():
            print("Você digitou uma consoante.")

        else:
            print("Caractere inválido.")

    """
    3. Se o usuário digitar uma palavra (mais de um caractere):

    a. Calcule e exiba o número de vogais na palavra.
    b. Calcule e exiba o número de consoantes na palavra.
    c. Exiba a palavra invertida.
    d. Informe se a palavra é um palíndromo (lê-se da mesma forma de trás para frente).     
    e. Peça ao usuário se deseja verificar outra letra ou palavra ou sair do programa.  

    """

