# Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista 
# (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
# - ValueError: se o usuário digitar um caracter
# - ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
# - IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
# - KeyboardInterrupt: caso o usuário interrompa a execução

try:
    # Cria uma lista vazia
    valores = []
    
    # Lê o primeiro valor do tipo float
    valor1 = float(input("Digite o primeiro valor: "))
    valores.append(valor1)
    
    # Lê o segundo valor do tipo float
    valor2 = float(input("Digite o segundo valor: "))
    valores.append(valor2)
    
    # Realiza a divisão dos dois valores
    resultado = valores[0] / valores[1]
    print(f"Resultado da divisão: {resultado}")

# Tratamento das exceções
except ValueError:
    print("Erro: Você deve digitar um número.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except IndexError:
    print("Erro: Tentativa de acesso a uma posição inexistente na lista.")
except KeyboardInterrupt:
    print("\nExecução interrompida pelo usuário.")

