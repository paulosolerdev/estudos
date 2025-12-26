s = 'Olá, mundo.'
print(s)
print(repr(s))
print(str(1/7))


x = 10 * 3.25
y = 200 * 200
s = f'O valor de x é {repr(x)} e de y é {repr(y)}...'
print(s)


# A repr() da string adiciona aspas e contrabarras:
ola = 'olá, mundo\n'
olas = repr(ola)
print(olas)


# O argumento de repr() pode ser qualquer objeto Python:
print(repr((x, y, ('spam', 'ovos'))))
