"""
Um objeto de função é um valor que pode ser atribuído a uma variável ou passado como
argumento. Por exemplo, do_twice é uma função que toma um objeto de função como
argumento e o chama duas vezes:

def do_twice(f):
f()
f()

Aqui está um exemplo que usa do_twice para chamar uma função chamada print_spam
duas vezes:

def print_spam():
    print('spam')
do_twice(print_spam)

1. Digite este exemplo em um script e teste-o.
2. Altere do_twice para que receba dois argumentos, um objeto de função e um valor, e
chame a função duas vezes, passando o valor como um argumento.
3. Copie a definição de print_twice que aparece anteriormente neste capítulo no seu
script.
4. Use a versão alterada de do_twice para chamar print_twice duas vezes, passando
'spam' como um argumento.
5. Defina uma função nova chamada do_four que receba um objeto de função e um
valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
haver só duas afirmações no corpo desta função, não quatro.

"""

# 1
# def do_twice(f):
#     f()
#     f()

# def print_spam():
#     print('spam')

# do_twice(print_spam)

#########################################################

# 2
# def do_twice(f, value):
#     f(value)
#     f(value)

# def print_spam(value):
#     print(value)

# do_twice(print_spam, 'spam')

#########################################################

# 3. Copie a definição de print_twice que aparece anteriormente neste capítulo no seu
# script.

# def print_twice(bruce):
#     print(bruce)
#     print(bruce)


#########################################################


# 4. Use a versão alterada de do_twice para chamar print_twice duas vezes, passando
# 'spam' como um argumento.

# def do_twice(f, value):
#     f(value)
#     f(value)

# def print_twice(value):
#     print(value)
#     print(value)

# do_twice(print_twice, 'spam')


#########################################################

# 5. Defina uma função nova chamada do_four que receba um objeto de função e um
# valor e chame a função quatro vezes, passando o valor como um parâmetro. Deve
# haver só duas afirmações no corpo desta função, não quatro.

def print_twice(value):
    print(value)
    print(value)

def do_twice(f, value):
    f(value)
    f(value)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'spam')

