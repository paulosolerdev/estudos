# def pergunta_ok(mensagem, tentativas=4, lembrete='Por favor, tente novamente: '):
#     while True:
#         resposta = input(mensagem).lower()
#         if resposta in {'s', 'sim', 'é'}:
#             return True
#         if resposta in {'n', 'não', 'nao', 'nah'}:
#             return False
#         tentativas -= 1
#         if tentativas < 0:
#             raise ValueError('resposta inválida de usuário')
#         print(lembrete)


# # --- Programa principal ---
# def main():
#     if pergunta_ok('Deseja continuar? (s/n): '):
#         print('Você escolheu continuar!')
#     else:
#         print('Você escolheu não continuar!')

# if __name__ == "__main__":
#     main()

#==========================================================#


i = 5

def f(arg=i):
    print(arg)

i = 6
f()
