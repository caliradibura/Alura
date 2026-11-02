# Autor: Carlos Lira
# Data: 01/11/2026

import os

def verificar_acesso():
    try:
        hora = int(input("Digite a hora atual (0-23): "))
        if hora < 0 or hora > 23:
            print("\nErro: A hora deve estar entre 0 e 23.")
            voltar_ao_menu()
        elif hora < 8 or hora >= 18:
            print("\nAcesso negado. O escritório está fechado.")
        else:
            print("\nAcesso permitido. Bem-vindo ao escritório!")
    except:
        print("\nOpção invalida digite apenas números inteiros.\n")
        voltar_ao_menu()

def main():
    os.system("cls")
    verificar_acesso()

def voltar_ao_menu():
    input("\nPressione qualquer tecla para voltar ao menu...\n")
    main()

if __name__ == "__main__":
    main()
