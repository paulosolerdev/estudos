from collections import deque

fila = deque(['Erik', 'João', 'Miguel'])
print(fila)
fila.append('Tiago')
fila.append('George')
print(fila)
fila.popleft()
print(fila)
fila.popleft()
print(fila)
