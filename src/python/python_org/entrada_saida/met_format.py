# print('{0} e {1}'.format('spam', 'eggs'))
# print('{1} e {0}'.format('spam', 'eggs'))


#=========================================================#


# print('Este {comida} está {adjetivo}.'.format(comida='spam', adjetivo='absolutamente horrível'))


#=========================================================#


# print('A história de {0}, {1} e {outro}.'.format('Bill', 'Manfred', outro='Georg'))


#=========================================================#


# tabela = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
#       'Dcab: {0[Dcab]:d}'.format(tabela))

# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**tabela))


#=========================================================#

# x = 10
# y = 20
# texto = 'olá'

# tabela = {k: str(v) for k, v in vars().items()}
# mensagem = " ".join([f'{k}: ' + '{' + k +'};' for k in tabela.keys()])
# print(mensagem.format(**tabela))


#=========================================================#


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
