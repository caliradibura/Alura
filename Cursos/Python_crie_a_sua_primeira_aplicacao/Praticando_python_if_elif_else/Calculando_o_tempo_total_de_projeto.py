# Autor: Carlos Lira
# Data: 01/11/2026

import os

alfabeto = ["A", "B", "C"]

def calcular_tempo_total():
    dias_das_atividades = []
    try:
        for letra in alfabeto:
            dias = int(input(f"Informe os dias para a atividade {letra}: "))
            if dias < 0:
                print("\nErro: Os dias não podem ser negativos.")
                input("\nPressione qualquer tecla para continuar...")
                main()  
            else:
                dias_das_atividades.append(dias) 
        
        total_dias = sum(dias_das_atividades)
        print(f"\nO tempo total do projeto é: {total_dias} dias.")  

    except:
        opcao_invalida()

def opcao_invalida():
    print("\nOpção invalida digite apenas números inteiros.\n")
    input("Pressione qualquer tecla para continuar...\n")
    main()

def main():
    os.system("cls")
    calcular_tempo_total()

if __name__ == "__main__":
    main()