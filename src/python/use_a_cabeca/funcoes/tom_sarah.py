def dobrar_lista(arg):
    # cria uma nova lista e faz arg apontar para ela
    arg = arg * 2
    print("Dentro da função:", arg)


numbers = [1, 2, 3]
dobrar_lista(numbers)
print("Fora da função:", numbers)

print("---")


def adicionar_numero(arg):
    # modifica a lista existente
    arg.append(4)
    print("Dentro da função:", arg)


numbers = [1, 2, 3]
adicionar_numero(numbers)
print("Fora da função:", numbers)
