## 1. Leia a idade do usuário e classifique-o em:
#- Criança – 0 a 12 anos
#- Adolescente – 13 a 17 anos
#- Adulto – acima de 18 anos
#-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida


# def retorna_categoria():
#     while True:
#         try:
#             idade = int(input('Digite sua idade:'))
            
#             if idade < 0:
#                 print('Idade inválida')
#             elif idade <= 12:
#                 print('Criança')
#             elif idade <= 17:
#                 print('Adolescente')
#             else:
#                 print('Adulto')
#             break  # Sai do loop se a idade for válida
#         except ValueError:
#             print("Por favor, digite um número válido.")

# retorna_categoria()


# Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
# - Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
# - Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
# - Se a média for maior do que 6.0, o aluno está aprovado
# - Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado


def notas_aluno():
    try:
        nota_M1 = float(input('Digite a nota do M1: '))
        nota_M2 = float(input('Digite a nota do M2: '))
        nota_M3 = float(input('Digite a nota do M3: '))
    except ValueError:
        print("Por favor, insira um valor numérico válido para as notas.")
        return

    media = (nota_M1 + nota_M2 + nota_M3) / 3

    if 0.0 <= media <= 4.0:
        print(f'Reprovado com média {media:.2f}')
    elif 4.1 <= media <= 6.0:
        print(f'Em exame com média {media:.2f}')
        try:
            nota_exame = float(input('Digite a nota do exame: '))
        except ValueError:
            print("Por favor, insira um valor numérico válido para a nota do exame.")
            return
        
        if nota_exame >= 6.0:
            print('Aprovado no exame')
        else:
            print('Reprovado no exame')
    elif media > 6.0:
        print(f'Aprovado com média {media:.2f}')
    else:
        print("Média inválida.")

notas_aluno()
        
        
    
    