# while True:
#     try:
#         x = int(input('Insira um número: '))
#         break
#     except ValueError:
#         print('Ops! Esse não é um número válido. Tente novamente.')

# print(f'Você inseriu o número {x}.')


#======================================================#


# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")


#======================================================#


try:
     raise Exception('spam', 'ovos')
except Exception as inst:
     print(type(inst))
     print(inst.args)
     print(inst)

     x, y = inst.args
     print(f'x = {x}')
     print(f'y = {y}')
