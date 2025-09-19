"""
26. Exercício "Jogo de Escape da Caverna"

Descrição: Você está preso em uma caverna com 3 portas misteriosas.

Cada porta pode te levar a um destino diferente. O objetivo é encontrar a
saída correta da caverna, mas existem armadilhas! O programa pedirá ao
usuário para escolher uma porta a cada rodada e o levará a diferentes cenários.

O jogo continua até que o usuário encontre a saída ou caia em uma armadilha.

Regras:

- Existem 3 portas: 1, 2 e 3.
- Apenas uma dessas portas leva à saída, as outras podem te levar de volta 
ao início ou te fazer perder o jogo.
- O jogo dará opções de escolha ao usuário, e ele poderá decidir qual porta abrir.
- O jogador pode continuar explorando as portas até encontrar a saída ou
ser pego por uma armadilha.
"""

import random

def jogar():

    print("Bem-vindo ao Jogo de Escape da Caverna!")
    print("Você está preso em uma caverna escura com 3 portas misteriosas.\n")

    porta_saida = random.randint(1, 3)

    jogando = True

    while jogando:

        print("Escolha uma porta para abrir (1, 2 ou 3):")

        escolha = int(input("Digite o número da porta:"))

        if escolha == porta_saida:

            print("Parabéns! Você encontrou a saída da caverna!\n")

            jogando = False

        else:

            destino = random.choice(["um túnel que te leva ao início",
                                     "uma armadilha perigosa! Você perdeu!"])
            
            if destino == "uma armadilha perigosa! Você perdeu!":

                print(f"Você caiu em uma armadilha perigosa! Você perdeu!\n")

                jogando = False

            else:

                print(f"Você encontrou {destino}, tente novamente!\n")


jogar()
