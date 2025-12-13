def f(ham: str, ovos: str = 'ovos') -> str:
    print("Anotações:", f.__annotations__)
    print("Argumentos:", ham, ovos)
    return ham + ' e ' + ovos

f('spam')
print(f('spam'))
