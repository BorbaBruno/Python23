# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
# A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

# def temperatura():
#     try:
#         celsius = float(input("Digite a temperatura em graus Celsius: "))
        
#         def converte_para_fahrenheit(celsius):
#             fahrenheit = (9 * celsius + 160) / 5
#             return fahrenheit
        
#         fahrenheit = converte_para_fahrenheit(celsius)
#         print(f"A temperatura de {celsius:.2f}°G é equivalente a {fahrenheit:.2f}°F")
    
#     except ValueError:
#         print("Por favor, insira um valor numérico!")
#         return temperatura()

# # Executar a função
# temperatura()


# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, 
# utilizando um automóvel que faz 12 Km por litro. 
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
# Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. 
# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

# Função para ler os valores do tempo e da velocidade média
def ler_valores():
    try:
        tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
        velocidade = float(input("Digite a velocidade média durante a viagem (em km/h): "))
        return tempo, velocidade
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return ler_valores()
    
# Função para calcular a distância percorrida
def calcular_distancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

# Função para calcular a quantidade de litros de combustível utilizada
def calcular_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

# Função para apresentar o resultado
def apresentar_resultado(tempo, velocidade, distancia, litros_usados):
    print(f"Velocidade média: {velocidade:.2f} km/h")
    print(f"Tempo gasto na viagem: {tempo:.2f} horas")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Quantidade de litros utilizada na viagem: {litros_usados:.2f} litros")
    
# Programa principal
def main():
    tempo, velocidade = ler_valores()
    distancia = calcular_distancia(tempo, velocidade)
    litros_usados = calcular_litros(distancia)
    apresentar_resultado(tempo, velocidade, distancia, litros_usados)
    
# Executar o programa principal
if __name__ == "__main__":
    main()
