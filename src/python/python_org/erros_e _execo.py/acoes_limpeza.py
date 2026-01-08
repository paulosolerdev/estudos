# try:
#     raise KeyboardInterrupt
# finally:
#     print('Adeus, mundo!')


#======================================================#


# def retorna_booleano():
#     try:
#         return True
#     finally:
#         return False


# print(retorna_booleano())



#======================================================#



# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print('division by zero!')
#     else:
#         print(f'result is {result}')
#     finally:
#         print('executing finally clause')


# # print(divide(2, 1))
# # print(divide(2, 0))
# print(divide('2', '1'))


#======================================================#



with open('arquivo_teste.txt') as f:
    for linha in f:
        print(f'{linha}')
