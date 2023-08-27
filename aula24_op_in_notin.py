# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4
# B r u n o
# -5-4-3-2-1



nome = 'Bruno'

print(nome[3])

print(nome[-2])

print('o' in nome)
print('a' in nome)

print('run' in nome)
print('run' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')




numero = 10
 
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')