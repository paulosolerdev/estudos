matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# print([[linha[i] for linha in matriz] for i in range(4)])


#==========================================#

transposta = []
for i in range(4):
    transposta.append([row[i] for row in matriz])

print(transposta)


#==========================================#

# E isso por sua vez é equivalente a:

#==========================================#

# transposta = []
# for i in range(4):
#     # as 3 linhas a seguir implementam uma compreensão de lista aninhada
#     linha_transposta = []
#     for linha in matriz:
#         linha_transposta.append(linha[i])
#     transposta.append(linha_transposta)

# print(transposta)


#==========================================#
#==========================================#


list(zip(*matriz))
print(list(zip(*matriz)))
