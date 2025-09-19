"""
27. Exercício: "Quiz de Matemática com Desafios"

Descrição: Crie um programa em Python que faça perguntas de matemática ao
usuário.

O programa apresentará uma série de perguntas aleatórias, e o jogador terá
que responder corretamente para continuar. A cada resposta certa, o nível
de dificuldade aumenta, e o jogador ganha pontos.

O jogo termina quando o jogador erra ou decide parar.

Regras:

- O jogo começa com operações simples (adição, subtração).
- Após cada resposta correta, o nível de dificuldade aumenta (multiplicação,
divisão, etc.).
- O jogador ganha pontos por cada resposta correta.
- O jogo termina quando o jogador erra uma resposta ou escolhe parar.

"""

import random

def quiz_matematica():

    pontuacao = 0

    nivel = 1

    continuar_jogo = True

    print("\nBem-vindo ao Quis de Matemática!\n")

    while continuar_jogo:

        if nivel == 1:

            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

            operacao = random.choice(['+', '-'])

            if operacao == '+':

                resultado = num1 + num2

            else:

                resultado = num1 - num2

        else:

            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)

            operacao = random.choice(['*', '/'])

            if operacao == '*':

                resultado = num1 * num2

            else:

                num1 = num1 * num2  # Garantir que a divisão seja exata
                resultado = num1 // num2

        print(f"Pergunta {nivel}: Quanto é {num1} {operacao} {num2}?")

        resposta = int(input("Sua resposta:"))

        if resposta == resultado:

            pontuacao += 10 * nivel

            print(f"Correto! Sua pontuação: {pontuacao} pontos.\n")

            nivel += 1

        else:

            print(f"Resposta incorreta! A resposta correta era {resultado}.")

            continuar_jogo = False

            break

        continuar = input("Deseja continuar? (s/n): ").lower()

        if continuar != 's':

            continuar_jogo = False

    print(f"Jogo encerrado! Sua pontuação final: {pontuacao} pontos.")


quiz_matematica()
