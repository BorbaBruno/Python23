# Operadores lógicos
# and (e) or (ou) not (nao)
# and - todas a condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrada [S]air: ')
senha = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha == senha_permitida:
    print('Entrando...')
else:
    print('Saindo...')