# if  / elif       / else
# se / se não se / se nao

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = False

# Quando for true, não executa mais o restante do bloco, ele sai do bloco.

if condicao1:
    print('Este é o código do IF')
elif condicao2:
    print('Este é o código do ELIF')
elif condicao3:
    print('Este é o outro ELIF')
elif condicao4:
    print('Este é o outro ELIF')
else:
    print('Nenhuma condição atentida')

if 10 == 10:
    print('Outro IF')

print('Fora do bloco condicional')