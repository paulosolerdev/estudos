# def arg_padrao(arg):
#     print(arg)

# def arg_somente_posicional(arg, /):
#     print(arg)

# def arg_somente_nomeado(*, arg):
#     print(arg)

# def exemplo_combinado(somente_posicional, /, padrão, *, somente_nomeado):
#     print(somente_posicional, padrão, somente_nomeado)


# arg_padrao(2)

# arg_padrao(arg=2)


def foo(nome, /, **kwds):
    return 'nome' in kwds

print(foo(1, **{'nome': 2}))
