cesta = {'maçã', 'laranja', 'maçã', 'pêra', 'laranja', 'banana'}
print(cesta)

print('laranja' in cesta)
print('crabgrass' in cesta)


# Demonstra operações de conjunto em letras únicas de duas palavras
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
