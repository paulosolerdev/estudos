def soma_digitos(n):
    return sum(int(digit) for digit in str(n))

print(soma_digitos(123))
print(soma_digitos(547))
print(soma_digitos(656))
