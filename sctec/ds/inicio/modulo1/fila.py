from collections import deque

fila = deque()

fila.append(1)
fila.append(2)
fila.append(3)
print(fila)

fila.popleft()
print(fila)
