# def fib(n):
#     """Imprime uma série de Fibonacci menor que n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()

# fib(200)

# fib(1000)

# fib(2000)

# print(fib)

# f = fib
# f(100)

# fib(0)
# print(fib(0))

#============================================================#

def fib2(n):
    """Retorna uma lista de Fibonacci menor que n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)
