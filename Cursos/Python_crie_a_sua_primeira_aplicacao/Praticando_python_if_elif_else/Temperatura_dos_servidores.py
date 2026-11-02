# Autor: Carlos Lira
# Data: 01/11/2026

import os 

def analise_da_temperatura():
    try:
        temperatura = float(input("Digite a temperatura atual: "))

        if temperatura > 25:
            print("\nAlerta! Temperatura acima do limite permitido.")
        else:
            print("\nTemperatura dentro do limite permitido.")
    except:
        opcao_invalida()

def main():
    os.system("cls")
    analise_da_temperatura()

def opcao_invalida():
    print("\nOpção invalida, digite apenas números inteiros ou decimais. \n")
    input("Pressione qualquer tecla para continuar...\n")
    main()

if __name__ == "__main__":
    main()
