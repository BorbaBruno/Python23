
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(a, b, c, d):
    return a * b * c * d

resultado = multiplica(1, 2, 3, 4)
print(resultado)

## OU

def multiplicar(*args):
    total = 1
    for numero in args:
        total*=numero
        return total

mult = multiplicar(1, 2, 3, 4, 5)
print(mult)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(a):
    if a % 2 == 0:
        return f'O valor {a} é Par'
    
    return f'O valor {a} é Impar'

par_impar = par_ou_impar(3)
print(par_impar)