import numpy as np

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# print(arr2[1, 2])

print(f'Shape da matriz: {arr2.shape}')
print(f'Número de elementos: {arr2.size}')
print(f"Tipo dos elementos: {arr2.dtype}")

arr1 = np.array([10, 20, 30, 40, 50])

print(f'{arr1 * 10}')

print(f'{arr2 * 2}')

print('Média: ')
print(f'{np.mean(arr1)}')

print('Mediana: ')
print(f'{np.median(arr1)}')

print('Desvio Padrão: ')
print(f'{np.std(arr1)}')
