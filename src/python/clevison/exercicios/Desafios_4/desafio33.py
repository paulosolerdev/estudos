"""
Exercício Análise de Desempenho do Aluno

Objetivo: Desenvolver um programa que avalie o desempenho de um aluno ao
longo dos bimestres. Para isso, o programa deve solicitar as quatro notas
bimestrais do aluno e, com base nelas, realizar as seguintes ações:

1. Calcular e exibir a média das notas.
2. Determinar e mostrar a maior e a menor nota entre as inseridas.
3. Com base na média, informar ao usuário se o aluno está aprovado, em
recuperação ou reprovado. Considere os seguintes critérios:
    - Aprovado: média >= 7
    - Em recuperação: 5 <= média < 7
    - Reprovado: média < 5

4. Calcular e mostrar a quantidade de notas que estão acima da média
calculada.

"""

# Solução do exercício

nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

# 1. Calcular e exibir a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"\nMédia das notas: {media:.2f}")


# 2. Determinar e mostrar a maior e a menor nota entre as inseridas
maior_nota = max(nota1, nota2, nota3, nota4)
menor_nota = min(nota1, nota2, nota3, nota4)
print(f"Maior nota: {maior_nota:.2f}")
print(f"Menor nota: {menor_nota:.2f}")


# 3. Informar ao usuário se o aluno está aprovado, em recuperação ou reprovado
if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Em recuperação")
else:
    print("Situação: Reprovado")

# 4. Calcular e mostrar a quantidade de notas que estão acima da média calculada
contador = 0

for nota in [nota1, nota2, nota3, nota4]:
    if nota > media:
        contador += 1
        print(f"Nota: {nota}")

print(f"Quantidade de notas acima da média: {contador}")
