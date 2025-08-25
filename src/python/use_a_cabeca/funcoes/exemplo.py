# def mudar_numero(n):
#     n = n + 1
#     print("Dentro:", n)

# x = 10
# mudar_numero(x)
# print("Fora:", x)


# def mudar_lista(lst):
#     lst.append(99)
#     print("Dentro:", lst)

# x = [1, 2, 3]
# mudar_lista(x)
# print("Fora:", x)


def redefinir_lista(lst):
    lst = [0, 0, 0]  # cria nova lista
    print("Dentro:", lst)


x = [1, 2, 3]
redefinir_lista(x)
print("Fora:", x)
