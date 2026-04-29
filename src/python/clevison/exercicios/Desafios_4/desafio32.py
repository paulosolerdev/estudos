"""
32. Exercício: "Jogo de Criação de Palavras"

Descrição: Neste jogo, o jogador recebe várias letras aleatórias e precisa
    formar a maior quantidade de palavras possível a partir dessas letras.

O jogador tem um limite de tempo para formar as palavras e ganha pontos por
    cada palavra válida. O jogo termina quando o tempo acaba, e a pontuação
    final é calculada com base no número de palavras formadas.

Regras:

- O jogador recebe 4 letras aleatórias.
- O jogador tem 60 segundos para formar quantas palavras puder com essas letras.
- Cada palavra formada corretamente dá pontos ao jogador.
"""

import random
import time
import threading

dicionario_palavras = ["rato", "esto", "ator", 'rosa', 'arte', 'teor',
                       'rota', 'ser', 'seta']

def gerar_letras_validas(dicionario):

    todas_letras = []

    palavra = random.choice(dicionario)

    todas_letras.extend(list(palavra))

    letras_unicas = list(set(todas_letras))

    return random.sample(letras_unicas, min(6, len(letras_unicas)))


def palavra_valida(palavra, letras_disponiveis):

    return all(palavra.count(letra) <= letras_disponiveis.count(letra) for letra in palavra)


def encerrar_jogo():

    global jogo_ativo

    jogo_ativo = False


def jogo_criacao_palavras():

    letras_disponiveis = gerar_letras_validas(dicionario_palavras)

    print(f'Bem-vindo ao Jogo de Criação de Palavras!')
    print(f'Você tem 60 segundos para formar palavras.')
    print(f'Letras disponíveis: {', '.join(letras_disponiveis).upper()}\n')

    global jogo_ativo

    jogo_ativo = True

    pontuacao = 0
    palavras_formadas = []

    temporizador = threading.Timer(60, encerrar_jogo)

    temporizador.start()

    while jogo_ativo:

        palavra = input('Digite uma palavra: ').lower()

        if not jogo_ativo:

            break

        if palavra in dicionario_palavras and palavra_valida(palavra, letras_disponiveis):

            if palavra not in palavras_formadas:

                palavras_formadas.append(palavra)

                pontuacao += 10

                print(f'Correto! +10 pontos. \n')

            else:

                print(f'Você já formou essa palavra. \n')

        else:

            print(f'Incorreto! Essa palavra não pode ser formada com as letras disponíveis.\n')

    
    palavras_possiveis = [
        palavra for palavra in dicionario_palavras

        if palavra_valida(palavra, letras_disponiveis)

    ]

    print(f'\nVocê formou {len(palavras_formadas)} palavras e ganhou {pontuacao} pontos.')

    print(f'Palavras que poderiam ser formadas com as letras disponíveis: {', '.join(palavras_possiveis)}')


jogo_criacao_palavras()
