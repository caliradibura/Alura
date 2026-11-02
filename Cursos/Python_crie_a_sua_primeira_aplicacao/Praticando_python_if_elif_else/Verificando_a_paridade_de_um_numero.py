# Autor: Carlos Lira
# Data: 02/11/2026

import os

def teste_de_paridade():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par")
        else:
            print(f"O número {numero} é impar")
    except:
        print("\nOpção invalida, digite um número")
        input("\nDigite qualquer tecla para continuar ...")
        main()

def main():
    os.system("cls")
    teste_de_paridade()

if __name__ == "__main__":
    main()