# Sistema de controle de estoque

# Bibliotecas
import os
from colorama import Fore, init
import json

# Para garantir que o colorama funcione corretamente
init(autoreset=True)

arquivo_estoque = 'estoque.json'

# Carregar estoque
def carregar_estoque():
    try:
        with open(arquivo_estoque, 'r') as e:
            return json.load(e)
    except FileNotFoundError:
        return []

estoque = carregar_estoque()

# Salvar estoque
def salvar_estoque():
    with open(arquivo_estoque, 'w') as e:
        json.dump(estoque, e, indent=2)


# Função de limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de pausa
def pausar():
    input(f'{Fore.GREEN}Digite ENTER para continuar!')


# Função de exibir menu
def exibir_menu():
    print(f'{Fore.GREEN}===== MENU =====')
    print(f'{Fore.CYAN}1. Adicionar produto')
    print(f'{Fore.CYAN}2. Atualizar produto')
    print(f'{Fore.CYAN}3. Excluir produto')
    print(f'{Fore.CYAN}4. Visualizar todo o estoque')
    print(f'{Fore.CYAN}0. Sair')

# Função de adicionar produtos
def adicionar_produtos():
    nome = input(f'{Fore.YELLOW}Digite o nome do produto: ')

    # Para tratar erro de numero inválido
    try:
        preco = float(input(f'{Fore.YELLOW}Digite o preço do produto: '))
        quantidade = int(input(f'{Fore.YELLOW}Digite a quantidade disponível no estoque: '))
    except ValueError:
        print(f'{Fore.RED}Erro: Digite apenas valores numéricos válidos!')
        return

    estoque.append({
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    })
    salvar_estoque()
    print(f"{Fore.YELLOW}Produto '{nome}' adicionado com sucesso!")
    

# Função de visualizar estoque
def visualizar_estoque():
    if not estoque:
        print(f'{Fore.RED}Estoque vazio!')
    else:
        print(f'{Fore.GREEN}===== ESTOQUE =====')
        for i, produto in enumerate(estoque, 1):
            print(f"{i}. {produto['nome']} | Preço: R${produto['preco']:.2f} | Quantidade: {produto['quantidade']}")
        
# Função de atualizar produtos
def atualizar_produto():
    if not estoque:
        print(f'{Fore.RED}Produto não encontrado! Tente a opção "4. Visualizar todo o estoque"')
        return
    
    busca_nome = input(f'{Fore.YELLOW}Digite o nome do produto que deseja atualizar: ')

    for produto in estoque:
        if produto['nome'].lower() == busca_nome.lower():
            print(f"{Fore.GREEN}Produto encontrado!: {produto['nome']} | Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']}")

            print(f'{Fore.GREEN}Itens disponíveis para atualização: ')
            print(f'{Fore.CYAN}1. Preço')
            print(f'{Fore.CYAN}2. Quantidade')
            print(f'{Fore.CYAN}0. Cancelar')

            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                novo_preco = float(input('Digite o novo preço: '))
                produto['preco'] = novo_preco
                salvar_estoque()
            elif opcao == '2':
                nova_qtdade = int(input('Digite a nova quantidade: '))
                produto['quantidade'] = nova_qtdade
                salvar_estoque()
            elif opcao == '0':
                print('Operação cancelada!')
                return
            else:
                print(f'{Fore.RED}Opção inválida, tente novamente.')
                return
            
            print(f'{Fore.YELLOW}Produto atualizado com sucesso!')
            return

#Função de excluir produtos
def excluir_produto(): 
    if not estoque:
        print(f'{Fore.RED}Produto não encontrado!')
        return

    nome_excluir = input(f'{Fore.YELLOW}Digite o nome do produto que deseja excluir: ')

    for i, produto in enumerate(estoque):
        if produto['nome'].lower() == nome_excluir.lower():
            print(f"{Fore.GREEN}Produto encontrado: {produto['nome']} | Preço: {produto['preco']} | Quantidade: {produto['quantidade']}")
            confirmar = input(f'{Fore.RED}Tem certeza que deseja excluir o produto {produto['nome']}? (sim/não): ').lower()
            if confirmar == 'sim':
                estoque.pop(i)
                print(f'{Fore.GREEN}Produto excluído com sucesso!')
            else:
                print(f'{Fore.RED}Exclusão cancelada.')
            return
            
    print(f'{Fore.RED}Produto não encontrado!')        
    salvar_estoque()

# Loop                                                                                                                                                                    
while True:
    limpar_tela()
    exibir_menu()
    opcao = input(f'{Fore.YELLOW}Digite a opção desejada: ')
    if opcao == '0':
        print(f'{Fore.RED}Saindo do sistema!')
        break 

    if opcao == '1':
        adicionar_produtos()

    elif opcao == '2':
        atualizar_produto()

    elif opcao == '3':
        excluir_produto()

    elif opcao == '4':
        visualizar_estoque()
    else:
        print(f'{Fore.RED}Opção inválida, tente novamente.')


    pausar()