##
# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, 
# utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
# Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, 
# com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, 
# tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

def calcular_consumo_combustivel(tempo_viagem, velocidade_media):
    # Calcular a distância percorrida
    distancia = tempo_viagem * velocidade_media
    
    # Calcular a quantidade de litros de combustível utilizada
    litros_usados = distancia / 12
    
    return velocidade_media, tempo_viagem, distancia, litros_usados

# Solicitar ao usuário o tempo gasto na viagem (em horas)
tempo_viagem = float(input("Digite o tempo gasto na viagem (em horas): "))

# Solicitar ao usuário a velocidade média durante a viagem (em km/h)
velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))

# Calcular os valores
velocidade_media, tempo_viagem, distancia, litros_usados = calcular_consumo_combustivel(tempo_viagem, velocidade_media)

# Exibir os resultados
print(f"Velocidade média: {velocidade_media} km/h")
print(f"Tempo gasto na viagem: {tempo_viagem} horas")
print(f"Distância percorrida: {distancia} km")
print(f"Quantidade de litros utilizada: {litros_usados:.2f} litros")