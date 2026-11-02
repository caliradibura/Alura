# Autor: Carlos Lira
# Data: 01/11/2026

import os

def opcao_invalida():
    print("Opção invalida digite apenas números inteiros.\n")
    input("Pressione qualquer tecla para continuar...\n")
    main()

def digitar_quantidade_vendida():
    try:
        maca = int(input("Digite a quantidade de maçãs vendidas: "))
        banana = int(input("Digite a quantidade de bananas vendidas: "))
        if maca > banana:
            print(f"\nVocê vendeu mais maçãs: {maca} maçãs vendidas.")
        elif banana > maca:
            print(f"\nVocê vendeu mais bananas: {banana} bananas vendidas.")
        else:
            print("\nVocê vendeu a mesma quantidade de maçãs e bananas.")
    except:
        opcao_invalida()

def main():
    os.system("cls")
    digitar_quantidade_vendida()

if __name__ == "__main__":
    main()