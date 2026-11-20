"""
Exercício: Nome na Vertical em Escada com Variações

Desenvolva um programa com as seguintes especificações:

1. Solicite ao usuário que digite seu nome.

2. Pergunte ao usuário como ele deseja ver o nome exibido:
a) Em formato de escada.
b) Em formato de escada invertida

3. Baseado na escolha do usuário, exiba o nome conforme solicitado.

Por exemplo, se o usuário digitar o nome "ANA" e escolher a opção de escada,
o programa deve exibir:

A
AN
ANA

Se escolher a opção de escada invertida, o programa deve exibir:

  A
 AN
ANA

"""

#Solução:

#1. Solicitar o nome ao usuário
nome = input("Digite seu nome: ")

"""
2. Pergunte ao usuário como ele deseja ver o nome exibido:
a) Em formato de escada.
b) Em formato de escada invertida.    
"""

escolha = input("Como você deseja ver o nome exibido? (a) Escada (b) Escada invertida: ") 


#3. Baseado na escolha do usuário, exiba o nome conforme solicitado.

if escolha == "a":
    for i in range(1, len(nome) + 1):
        print(nome[:i])
elif escolha == "b":
    for i in range(len(nome), 0, -1):
        print(" " * (len(nome) - i) + nome[:i])

        