"""
29. Exercício: "Criptografia de Substituição"

Descrição: Neste exercício, o jogador deve decifrar uma mensagem criptografada
usando uma substituição de letras. O programa gera uma mensagem oculta, onde
cada letra foi substituída por outra letra.

O jogador deve tentar adivinhar qual é a substituição correta, letra por letra,
para revelar a mensagem original. A cada tentativa, o programa revela as
letras corretas ou informa se o jogador errou.

Regras:

- O jogador recebe uma mensagem criptografada com substituição de letras 
(exemplo: 'A' foi substituída por 'D', 'B' por 'E', etc.).
- O jogador deve tentar adivinhar a correspondência entre as letras.
- O programa verifica a resposta e atualiza a mensagem com as letras corretas
a cada tentativa.
- O jogo termina quando a mensagem inteira for decifrada.
"""

import random
import string


def gerar_criptografia():

    letras = list(string.ascii_lowercase)

    random.shuffle(letras)

    substituicao = {chr(i +97): letras[i] for i in range(26)}

    return substituicao


def criptografar_mensagem(mensagem, substituicao):

    return ''. join(substituicao.get(c, c) for c in mensagem)


def decifrar_mensagem(mensagem, mapeamento_usuario):

    return ''.join(mapeamento_usuario.get(c, '*') if c.isalpha() else c for c in mensagem)


def criptografia():

    mensagem_original = "este e um teste"

    substituticao = gerar_criptografia()

    mensagem_criptografada = decifrar_mensagem(mensagem_original, substituticao)

    print(f"Mensagem criptografada: {mensagem_criptografada}")

    mapeamento_usuario = {}

    mensagem_decifrada = decifrar_mensagem(mensagem_criptografada, mapeamento_usuario)

    print(f'Mensagem decifrada até agora: {mensagem_decifrada}\n')

    while True:

        letra_criptografada = input("Digite a letra criptografada que você quer decifrar:").lower()

        letra_real = input(f'Qual é a letra original correspontente a "(letra_criptografada)"? ').lower()

        mapeamento_usuario[letra_criptografada] = letra_real

        mensagem_decifrada = decifrar_mensagem(mensagem_criptografada, mapeamento_usuario)

        print(f"\nMensagem decifrada até agora: {mensagem_decifrada}\n")

        if '*' not in mensagem_decifrada:

            print("Parabéns! Você decifrou a mensagem!")

            break


criptografia()
