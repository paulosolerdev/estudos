# 1.

"""
pi = 3.14
r = 5
volume = (4 / 3) * pi * (r**3)

print(volume)
"""

# =========================================#


# 2.

""" preco_capa = 24.95
desconto = 0.40
quantidade = 60

frete_primeiro = 3.00
frete_adicional = 0.75

preco_unitario = preco_capa * (1 - desconto)
subtotal_livros = preco_unitario * quantidade
custo_frete = frete_primeiro + (quantidade - 1) * frete_adicional
custo_total = subtotal_livros + custo_frete

print(f"Preço unitário no atacado: R$ {preco_unitario:.2f}")
print(f"Subtotal dos {quantidade} livros: R$ {subtotal_livros:.2f}")
print(f"Custo do transporte: R$ {custo_frete:.2f}")
print(f"Custo total de atacado: R$ {custo_total:.2f}")
 """

# 3.

# Converte o horário de saída (6:52) para segundos desde a meia-noite
saida_segundos = (6 * 3600) + (52 * 60)

# Calcula a duração de cada trecho em segundos
trecho_1 = 1 * (8 * 60 + 15)
trecho_2 = 3 * (7 * 60 + 12)
trecho_3 = 1 * (8 * 60 + 15)

tempo_corrida = trecho_1 + trecho_2 + trecho_3
chegada_segundos = saida_segundos + tempo_corrida

# Converte de volta para horas, minutos e segundos
horas = chegada_segundos // 3600
minutos = (chegada_segundos % 3600) // 60
segundos = chegada_segundos % 60

print(f"Tempo total de corrida: {tempo_corrida // 60}min {tempo_corrida % 60}s")
print(f"Horário de chegada: {horas:02d}:{minutos:02d}:{segundos:02d}")
