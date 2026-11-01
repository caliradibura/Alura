import os

restaurantes = [{"nome" : "Praça", "categoria" : "Japonesa", "ativo" : False},
                {"nome" : "Pizza Suprema", "categoria" : "Pizza", "ativo" : True},
                {"nome" : "Cantina", "categoria" : "Italiano", "ativo" : False}]

def exibir_nome_do_programa():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)
    
def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair")

def finalizar_app():
    exibir_subtitulo("Finalizando o app...")
    
def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu ")
    main()

def opcao_invalida():
    exibir_subtitulo("Opção invalida!")
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f"{texto}\n")

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastrar novo restaurante")
    nome_do_restaurante = input("Digita o nome do restauramte que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")
    
    for restaurante in restaurantes:
        nome = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"- {nome} | {categoria} | {ativo}")

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("\nEscolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()    
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()