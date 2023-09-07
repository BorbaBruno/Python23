lista_compras = []

def adicionar_item(item):
    lista_compras.append(item)
    print(f"Item '{item}' adicionado à lista de compras.")

def pesquisar_item(item):
    if item in lista_compras:
        print(f"O item '{item}' está na lista de compras.")
    else:
        print(f"O item '{item}' não está na lista de compras.")

def deletar_item(item):
    try:
        lista_compras.remove(item)
        print(f"Item '{item}' removido da lista de compras.")
    except ValueError:
        print(f"O item '{item}' não está na lista de compras.")

def exibir_lista():
    if lista_compras:
        print("Lista de compras:")
        for item in lista_compras:
            print(item)
    else:
        print("A lista de compras está vazia.")

while True:
    print("\n--- MENU ---") 
    print("1. Adicionar item")
    print("2. Pesquisar item")
    print("3. Deletar item")
    print("4. Exibir lista de compras")
    print("5. Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        item = input("Digite o item a ser adicionado: ")
        adicionar_item(item)
    elif escolha == "2":
        item = input("Digite o item a ser pesquisado: ")
        pesquisar_item(item)
    elif escolha == "3":
        item = input("Digite o item a ser deletado: ")
        deletar_item(item)
    elif escolha == "4":
        exibir_lista()
    elif escolha == "5":
        break
    else:
        print("Opção inválida. Digite novamente.")

print("Programa encerrado.")





"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
"""
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
    """