"""

Escreva uma função chamada right_justify, que receba uma string chamada s
como parâmetro e exiba a string com espaços suficientes à frente para que a 
última letra da string esteja na coluna 70:

"""

def right_justify(s):
    """Exibe s deslocada para a direita até a última letra ficar na coluna 70."""
    espacos = 70 - len(s)
    print(' ' * espacos + s)

right_justify('allen')
right_justify('x')
right_justify('capivara')
