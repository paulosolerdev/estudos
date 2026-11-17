"""
Exercício - Análise Comparativa e Estatística de Números

Objetivo: Desenvolver um programa que obtenha do usuário dez números e
realize análises estatísticas e matemáticas com base nos valores inseridos.

Instruções:

1. Solicite ao usuário que insira dez números.
2. Determine e exiba qual é o maior número.
3. Determine e exiba qual é o menor número.
4. Calcule e exiba a média dos números inseridos.
5. Informe quantos dos números são pares.
6. Informe quantos dos números são positivos.
7. Calcule e exiba a variação (diferença) entre o maior e o menor número.
8. Mostre a soma dos números que são maiores que a média calculada.
9. Informe quantos dos números são negativos.

Observações: O programa deve considerar que usuário fornecerá apenas valores
numéricos válidos. Em todas as operações, os resultados devem ser exibidos
com até duas casas decimais, quando aplicável.

"""

# Solução do exercício

# 1. Solicitar ao usuário que insira dez números
numeros = []
for i in range(1, 11):
    num = int(input(f"Informe o {i}º número: "))
    numeros.append(num)


# 2. Determinar e exibir qual é o maior número
maior_numero = max(numeros)
print(f"O maior número é: {maior_numero}")


# 3. Determinar e exibir qual é o menor número
menor_numero = min(numeros)
print(f"O menor número é: {menor_numero}")


# 4. Calcular e exibir a média dos números inseridos
media = sum(numeros) / len(numeros)
print(f"A média dos números é: {media:.2f}")


# 5. Informar quantos dos números são pares

pares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1

print(f"{pares} números informados são pares.")


# 6. Informar quantos dos números são positivos
positivos = 0

for num in numeros:
    if num > 0:
        positivos += 1

print(f"{positivos} números informados são positivos.")


# 7. Calcular e exibir a variação (diferença) entre o maior e o menor número
variacao = maior_numero - menor_numero
print(f"A variação entre o maior e o menor número é: {variacao}")


# 8. Mostrar a soma dos números que são maiores que a média calculada
soma_maiores_que_media = sum(num for num in numeros if num > media)
print(f"A soma dos números maiores que a média é: {soma_maiores_que_media}")


# 9. Informar quantos dos números são negativos
negativos = 0
for num in numeros:
    if num < 0:
        negativos += 1
print(f"{negativos} números informados são negativos.")
