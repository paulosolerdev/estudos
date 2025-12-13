for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'igual a', x, '*', n//x)
            break
    else:
        # a iteração passou direto sem encontrar um fator
        print(n, 'é um número primo')
