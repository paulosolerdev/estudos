"""
Exercício Cálculo do Salário com Horas Extras e Imposto de Renda

Objetivo: Desenvolver um programa que ajude o usuário a entender
a composição do seu salário mensal. O programa deve considerar o
valor recebido por hora, as horas trabalhadas no mês, o cálculo de
horas extras e o desconto do imposto de renda.

Instruções:

1. Solicite ao usuário o valor que ele ganha por hora.
2. Pergunte quantas horas foram trabalhadas no mês.
3. Calcule o salário bruto multiplicando o valor por hora pelas
horas trabalhadas.
4. Se o usuário tiver trabalhado mais de 160 horas no mês,
calcule o valor das horas extras. Cada hora extra deve ser compensada
com um adicional de 50% sobre o valor da hora normal.
5. Calcule o imposto de renda sobre o salário (considerando as horas
extras). O imposto de renda tem uma taxa fixa de 11% sobre o salário.
6. Mostre ao usuário uma descrição detalhada contendo:
    - Salário bruto (sem considerar horas extras)
    - Valor das horas extras (se houver)
    - Valor do imposto de renda
    - Salário líquido (salário bruto + horas extras - imposto de renda)
7. Certifique-se de que todos os valores monetários sejam exibidos
com duas casas decimais.
"""

# Solução do exercício

# 1. Solicitar ao usuário o valor que ele ganha por hora
valor_hora = float(input("Digite o valor que você ganha por hora: "))

# 2. Perguntar quantas horas foram trabalhadas no mês
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# 3. Calcular o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# 4. Calcular o valor das horas extras, se houver
horas_extras = 0
if horas_trabalhadas > 160:
    horas_extras = horas_trabalhadas - 160
    valor_horas_extras = horas_extras * (valor_hora * 1.5)
else:
    valor_horas_extras = 0

# 5. Calcular o imposto de renda sobre o salário (considerando as horas extras)
salario_total = salario_bruto + valor_horas_extras
imposto_renda = salario_total * 0.11

# 6. Calcular o salário líquido
salario_liquido = salario_total - imposto_renda

# 7. Mostrar ao usuário uma descrição detalhada
print("\nDescrição detalhada do salário:")
print(f"Salário bruto (sem considerar horas extras): R$ {salario_bruto:.2f}")
print(f"Valor das horas extras: R$ {valor_horas_extras:.2f}")
print(f"Valor do imposto de renda: R$ {imposto_renda:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
