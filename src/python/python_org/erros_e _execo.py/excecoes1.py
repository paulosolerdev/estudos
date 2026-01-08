import sys

# try:
#     f = open('arquivo_teste.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print(f'Erro de E/S: {err}')
# except ValueError:
#     print('Não foi possível converter dados para um inteiro.')
# except Exception as err:
#     print(f'Não esperava {err=}, {type(err)=}')
#     raise


# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print(f'Não foi possível abrir o arquivo: {arg}')
#     else:
#         print(f'{arg} tem {len(f.readlines())} linhas.')
#         f.close()


# for arg in sys.argv[1:]:
#     try:
#         with open(arg, 'r') as f:
#             print(arg, 'tem', len(f.readlines()), 'linhas')
#     except OSError:
#         print('não foi possível abrir', arg)


def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print(f'Tratando o erro de tempo de execução: {err}')
