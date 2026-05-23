import matplotlib.pyplot as plt

# Criando um gráfico de linha
# plt.plot([1, 3, 5], [2, 6, 7])

# plt.show()

# Dados
x = ['Maçãs', 'Laranjas', 'Uvas', 'Bananas', 'Pêssegos']
y = [10, 15, 20, 25, 30]

plt.bar(x, y)

# Adicionando rótulos
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quantidade de Frutas')

plt.show()
