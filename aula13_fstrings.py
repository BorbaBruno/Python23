nome = 'Bruno Rafael'
altura = 1.70
peso = 90
imc = peso / (altura * altura)      #... #Elipses/Placeholder    #IMC = peso / (altura x altura)

print(nome, 'tem', altura, 'de altura' )
print('pesa', peso,'KG e seu IMC é', imc)


#f-strings

linha_1 = f'{nome} tem {altura:.2f} de altura' 
linha_2 = f'pesa {peso}KG e seu IMC é: {imc:.2f}'
print(linha_1)
print(linha_2)