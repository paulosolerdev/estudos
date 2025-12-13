frutas = ['laranja', 'maçã', 'pera', 'banana', 'kiwi', 'maçã', 'banana']

print(frutas.count('tangerina'))

print(frutas.index('banana'))

print(frutas.index('banana', 4))  # Começa a buscar a partir do índice 4

print(frutas.reverse())

print(frutas)

print(frutas.append('uva'))

print(frutas)

print(frutas.sort())

print(frutas)

print(frutas.pop())


"""

Forma correta de testar no script
❌ Forma errada (gera None)
print(frutas.sort())

✅ Forma certa
frutas.sort()
print(frutas)

"""
