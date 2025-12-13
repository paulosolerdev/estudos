# def f(a, L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))


#================================#


# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))


#================================#


def f(a, L=[]):
    L.append(a)
    print('id(L)=', id(L))
    return L

f(1)
f(2)
f(3)
