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
