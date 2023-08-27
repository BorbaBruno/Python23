"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::] # início, fim, passo  [4:] do indice 4 até o fim / [:5] do início até o indice 5
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[0:9:1])
print(len(variavel))