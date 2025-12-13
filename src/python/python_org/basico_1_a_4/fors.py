# produtos = {'arroz':10, 'tv':3000, 'banana':5, 'celular':1500, 'notebook':4000}

# for produto, preco in produtos.copy().items():
#     if preco < 100:
#         del produtos[produto]

# print(produtos)


#=====================================================#


produtos = {'arroz':10, 'tv':3000, 'banana':5, 'celular':1500, 'notebook':4000}

produtos_filtrados = {}

for produto, preco in produtos.items():
    if preco >= 10:
        produtos_filtrados[produto] = preco

print(produtos_filtrados)
print(produtos)
