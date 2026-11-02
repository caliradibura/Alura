# Autor: Carlos Lira
# Data: 01/11/2026

import os

def diagnostico_imc():
    try:
        peso = float(input("Digite o seu peso (KG): "))
        altura = float(input("Digite a sua altura (M): "))

        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            print(f"\nSeu IMC é {imc:.2f}. Você está abaixo do peso.")
        elif 18.5 <= imc < 25:
            print(f"\nSeu IMC é {imc:.2f}. Você está com o peso normal.")
        elif 25 <= imc < 30:
            print(f"\nSeu IMC é {imc:.2f}. Você está com sobrepeso.")
        elif 30 <= imc < 35:
            print(f"\nSeu IMC é {imc:.2f}. Você está com obesidade grau 1.")
        else:
            print(f"\nSeu IMC é {imc:.2f}. Você está com obesidade grau 2 ou 3.")
    except:
        print("\nOpção invalida, digite apenas números inteiros ou decimais. \n")
        input("Pressione qualquer tecla para continuar...\n")
        main()

def main():
    os.system("cls")
    diagnostico_imc()

if __name__ == "__main__":
    main()