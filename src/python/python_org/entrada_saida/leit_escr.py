# with open('arquivo_teste.txt', encoding='utf-8') as f:
#     read_data = f.read()
#     print(read_data)


# with open('arquivo_teste.txt', encoding='utf-8') as f:
#     for line in f:
#         print(line)


# with open('arquivo_teste.txt', encoding='utf-8') as f:
#     read_data = f.read()

# for line in read_data.splitlines():
#     print(line)


# with open('arquivo_teste.txt', encoding='utf-8') as f:
#     read_data = f.read()
#     f.seek(0)

#     for line in f:
#         print(line, end='')


# f = open('arquivo_teste.txt', 'rb+')
# print(f.write(b'0123456789abcdef'))
# print(f.seek(5))
# print(f.read(1))
# print(f.seek(-3, 2))
# print(f.read(1))
# f.close()


import json
x = [1, 'lista', 'simples']
print(json.dumps(x))
