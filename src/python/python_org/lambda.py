import locale
print(locale.getlocale())
print(locale.getdefaultlocale())
print(locale.setlocale(locale.LC_ALL, ""))
#================================================#

# def cria_incrementador(n):
#     return lambda x: x + n

# f = cria_incrementador(42)

# print(f(0))
# print(f(1))


#================================================#


# pairs = [(1, 'um'), (2, 'dois'), (3, 'três'), (4, 'quatro')]
# pairs.sort(key=lambda pair: pair[1])

# print(pairs)


#================================================#


pairs = [(1, 'um'), (2, 'dois'), (3, 'três'), (4, 'quatro')]
pairs.sort(key=lambda p: locale.strxfrm(p[1]))

print(pairs)
