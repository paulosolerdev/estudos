# f = open('arquivo_teste.txt', 'w', encoding='utf-8')


with open('arquivo_teste.txt', encoding='utf-8') as f:
    read_data = f.read()

# print(f.closed)
# print(read_data)
# print(read_data)

for line in f:
    print(line, end='')
