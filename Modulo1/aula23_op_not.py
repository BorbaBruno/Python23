# Usado para inverter a expressão quando necessário.

senha = input('Senha: ')

if senha != '123456':
    print('Senha incorreta.')

if not senha:
    print('Você não digitou nada.')


print(not True) # False
print(not False) # True


