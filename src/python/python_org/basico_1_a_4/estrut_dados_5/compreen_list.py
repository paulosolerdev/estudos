# quadrados = []

# for x in range(10):
#     quadrados.append(x**2)

# print(quadrados)


#=========================================#


# quadrados = [x**2 for x in range(10)]
# print(quadrados)


#=========================================#
#=========================================#


# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])


#=========================================#


# combos = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combos.append((x, y))

# print(combos)


# combos = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combos.append((x, y))

# print(combos)
#=========================================#


# vec = [-4, -2, 0, 2, 4]
# [x*2 for x in vec]
# print([x*2 for x in vec])

# [x for x in vec if x >= 0]
# print([x for x in vec if x >= 0])

# [abs(x) for x in vec]

# frutafresca = [' banana', ' bada-de-logan ', 'maracujá  ']
# [arma.strip() for arma in frutafresca]
# print([arma.strip() for arma in frutafresca])

# [(x, x**2) for x in range(6)]
# print([(x, x**2) for x in range(6)])

# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [num for elem in vec for num in elem]
# print([num for elem in vec for num in elem])


#=========================================#
#=========================================#


from math import pi

[str(round(pi, i)) for i in range(1, 6)]
print([str(round(pi, i)) for i in range(1, 6)])
