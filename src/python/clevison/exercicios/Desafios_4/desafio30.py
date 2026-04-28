def tabuada_interativa():

    print("Bem vindo à Calculadora de Tabuada Interativa!")

    numero = int(input("Digite um número para o qual você deseja praticar a tabuada: "))

    acertos = 0

    for i in range(1, 11):

        resposta_correta = numero * i

        resposta_usuario = int(input(f"Quanto é {numero} x {i}? "))

        if resposta_usuario == resposta_correta:

            print("Correto!")
            acertos += 1

        else:

            print(f"Incorreto. A resposta correta é {resposta_correta}.\n")

    print(f"Parabéns! Você acertou {acertos} de 10 perguntas.")


tabuada_interativa()
