# Dados iniciais
distancia_km = 10
tempo_minutos = 42
tempo_segundos = 42

# Conversões de unidade
km_por_milha = 1.609344
distancia_milhas = distancia_km / km_por_milha

tempo_total_segundos = (tempo_minutos * 60) + tempo_segundos
tempo_total_horas = tempo_total_segundos / 3600

# 1. Cálculo do passo médio (tempo por milha)
segundos_por_milha = tempo_total_segundos / distancia_milhas
passo_minutos = int(segundos_por_milha // 60)
passo_segundos = segundos_por_milha % 60

# 2. Cálculo da velocidade média (milhas por hora)
velocidade_mph = distancia_milhas / tempo_total_horas

# Exibição dos resultados
print(f"Distância em milhas: {distancia_milhas:.4f} milhas")
print(f"Passo médio: {passo_minutos} minutos e {passo_segundos:.2f} segundos por milha")
print(f"Velocidade média: {velocidade_mph:.2f} mph")
