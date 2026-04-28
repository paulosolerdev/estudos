"""

32. Exercício: "Jogo da Memória Numérica"

Descrição: Neste jogo, o jogador deve memorizar uma sequência de números que
    será exibida por alguns segundos. Após o tempo, a sequência desaparece e o
    jogador deve tentar reproduzir a sequência corretamente.

O jogo aumenta a dificuldade a cada rodada, adicionando um número a mais 
    à sequência.

Regras:

- O jogo começa com uma sequência de 3 números.
- O jogador tem 3 segundos para memorizar a sequência antes que ela desapareça.
- A cada rodada, a sequência aumenta em um número, e o jogador deve tentar
    lembrá-la corretamente.
- O jogo continua até o jogador errar a sequência.

"""

import random
import time

def jogo_memoria_numerica():

    print("Bem-vindo ao Jogo da Memória Numérica!")
    print("Memorize a sequência de números que será exibida.")
    print("Você tem 3 segundos para memorizar cada sequência.\n")

    rodada = 1
    sequencia = []

    while True:

        # Gerar um número aleatório e adicioná-lo à sequência
        novo_numero = random.randint(0, 9)
        sequencia.append(novo_numero)

        # Exibir a sequência para o jogador
        print(f"Rodada {rodada}: {' '.join(map(str, sequencia))}")
        time.sleep(3)  # Esperar 3 segundos
        print("\033c", end="")  # Limpar a tela

        # Solicitar ao jogador que reproduza a sequência
        resposta_usuario = input("Digite a sequência de números (separados por espaço): ")
        resposta_usuario_lista = list(map(int, resposta_usuario.split()))

        # Verificar se a resposta do usuário está correta
        if resposta_usuario_lista == sequencia:
            print("Correto! Vamos para a próxima rodada.\n")
            rodada += 1
        else:
            print(f"Incorreto. A sequência correta era: {' '.join(map(str, sequencia))}.")
            print(f"Você chegou até a rodada {rodada}.")
            break

jogo_memoria_numerica()
