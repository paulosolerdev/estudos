"""
1. Crie um dataframe que contenha algumas linhas e colunas de dados sobre
funcionários; inclua as colunas: nome, endereço, data de nascimento,
data de admissão, salário e cargo;

2. Em seguida, mostre na tela todas as linhas da coluna de data de admissão.
"""

import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Endereço': ['Rua A, 123', 'Rua B, 456', 'Rua C, 789', 'Rua D, 101', 'Rua E, 202'],
    'Data de Nascimento': ['1990-01-01', '1985-05-15', '1992-08-20', '1988-12-10', '1995-03-25'],
    'Data de Admissão': ['2015-06-01', '2010-09-15', '2018-11-20', '2012-04-10', '2020-01-05'],
    'Salário': [5000, 6000, 5500, 7000, 4500],
    'Cargo': ['Analista', 'Gerente', 'Desenvolvedor', 'Designer', 'Assistente']
}

df = pd.DataFrame(data)

print(df['Data de Admissão'])
