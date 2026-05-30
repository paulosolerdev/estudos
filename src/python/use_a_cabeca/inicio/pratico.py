"""
Exercício prático agora

Crie um arquivo exercicio.py com esse desafio:

Crie uma lista com 5 títulos de ebooks.
Mostre cada um numerado (1. Título, 2. Título...)
Pergunte ao usuário qual número ele quer ver.
Mostre o título escolhido.

"""

ebooks = [
    "Python para Iniciantes",
    "Python para Desenvolvedores",
    "Python para Data Science",
    "Python para Web",
    "Python para Automatização"
]

for i, ebook in enumerate(ebooks, start=1):
    print(f"{i}. {ebook}")

escolha = int(input("Qual ebook você quer ver? "))
print(f"Você escolheu: {ebooks[escolha - 1]}")
