# Autor: Carlos Lira
# Data: 02/11/2026

import os

def calculo_pedagio():
    try:
        distancia_percorida = float(input("Digite a distância percorrida em (Km): "))

        if distancia_percorida <= 0:
            opcao_invalida()
        elif distancia_percorida > 0 and distancia_percorida < 100:
            print(f"Você percorreu {distancia_percorida}, e pagara R$ 10,00")
        elif distancia_percorida >= 100 and distancia_percorida <= 200:
            print(f"Você percorreu {distancia_percorida}, e pagara R$ 20,00")
        else:
            print(f"Você percorreu {distancia_percorida}, e pagara R$ 30,00")
    except:
        opcao_invalida()

def main():
    os.system("cls")
    calculo_pedagio()

def opcao_invalida():
    os.system("cls")
    print("Digite uma distância valida\n")
    input("Digite qualquer tecla para continuar\n")
    main()

if __name__ == "__main__":
    main()