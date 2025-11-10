"""
28. Exercício: "Construa a Palavra"

Descrição: Neste jogo, o computador começa com uma letra válida, que pertence
    a pelo menos uma das palavras do dicionário.

O jogador deve continuar construindo a palavra com letras que ele acredita que
    completam essa palavra válida.

O jogo termina quando o jogador finaliza a palavra ou comete um erro, e o 
    programa verifica se a palavra construída é válida.

Regras Ajustadas:

- O jogo começa com uma letra válida que está no dicionário de palavras.
- O jogador deve adicionar letras para formar uma palavra.
- Se a letra escolhida não for possível para formar uma palavra válida, o jogador
    será avisado.
- O jogador pode "finalizar" a palavra quando achar que ela está completa.
"""

import random

dicionario_palavras = ["casa", "carro", "jogo", "animal", "caminho", "livro",
                       "escola", "planta"]


def escolher_letra_inicial(dicionario):

    palavra_escolhida = random.choice(dicionario)

    return palavra_escolhida[0].upper()

def construir_palavra():

    letra_inicial = escolher_letra_inicial(dicionario_palavras)

    print(f"Bem-vindo ao jogo 'Construa a Palavra'!")
    print(f"A primeira letra é:\"\n")

    palavra_atual = letra_inicial.lower()

    while True:

        letra = input(f"Digite uma letra para adicionar ou 'fim' para terminar a palavra: ").lower()

        if letra == 'fim':

            break

        elif letra.isalpha() and len(letra) == 1:

            palavra_atual += letra

            print(f"A palavra atual é: \"{palavra_atual}\"\n")

        else:

            print("Entrada inválida. Digite uma letra ou 'fim'.")

    if palavra_atual in dicionario_palavras:

        print(f"Parabéns! \"{palavra_atual} \" é uma palavra válida! Você ganhou 10 pontos.")

    else:

        print(f'\'{palavra_atual}\' não é uma palavra válida. Tente novamente!')


construir_palavra()
