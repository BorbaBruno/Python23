# Operadores lógicos
# and (e) or (ou) not (nao)
# and - todas a condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrada [S]air: ')
senha = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrando...')
else:
    print('Saindo...')


# Avaliação de curto circuito 
print(True or False) #True

print(0 or False or 0)

senha = input('Senha: ') or 'Sem senha'
print(senha)