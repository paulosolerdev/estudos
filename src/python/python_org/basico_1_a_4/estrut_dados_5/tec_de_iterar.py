# cavaleiros = {'gallahad': 'o puro', 'robin': 'o bravo'}

# for k, v in cavaleiros.items():
#     print(f'{k} {v}')


##==========================================##


###==========================================##
#for i, v in enumerate(['jogo', 'da', 'velha']):
##     print(i, v)


##==========================================##


# perguntas = ['Nome', 'Missão', 'Cor favorita']
# respostas = ['Lancelot', 'o santo graal', 'azul']
# for q, a in zip(perguntas, respostas):
#     print(f'{q}? É {a}.')


##==========================================##


# for i in reversed(range(1, 10, 2)):
#     print(i)


##==========================================##


# cesta = ['maçã', 'laranja', 'maçã', 'pêra', 'laranja', 'banana']

# for i in sorted(set(cesta)):
#     print(i)


##==========================================##


import math

dados_brutos = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
dados_filtrados = []

for valor in dados_brutos:
    if not math.isnan(valor):
        dados_filtrados.append(valor)

print(dados_filtrados)
