# print(list(range(3, 6)))

# args = [3, 6]
# print(list(range(*args)))


#============================================#


def papagaio(voltagem, estado='um cadáver', ação='voar'):
    print('-- Este papagaio não conseguiria', ação, end=' ')
    print('nem se você desse um choque de', voltagem, 'de volts nele.', end=' ')
    print('Ele', estado, '!')

d = {'voltagem': 'quatro milhões', 'estado': 'está realmente morto', 'ação': 'voar'}

print(papagaio(**d))
