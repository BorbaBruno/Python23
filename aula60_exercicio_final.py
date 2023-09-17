"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

def validar_cpf(cpf):
     # Removendo caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Cálculo do primeiro dígito verificador
    multiplicadores = range(10, 1, -1)
    soma = sum(int(c) * m for c, m in zip(cpf[:9], multiplicadores))
    resto = soma % 11
    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    # Verificando o primeiro dígito verificador
    if int(cpf[9]) != primeiro_digito:
        return False
    
    # Cálculo do segundo dígito verificador
    multiplicadores = range(11, 1, -1)
    soma = sum(int(c) * m for c, m in zip(cpf[:10], multiplicadores))
    resto = soma % 11
    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    # Verificando o segundo dígito verificador
    if int(cpf[10]) != segundo_digito:
        return False

    return True

# Exemplo de uso
cpf = input("Digite um CPF: ")
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")