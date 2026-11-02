# Autor: Carlos Lira
# Data: 01/11/2026

import os 

def analise_do_orcamento():
    try:
        despesas = float(input("Digite o total de despesas do mês (R$): "))

        if despesas > 3000:
            print("\nAlerta! Você ultrapassou o limite do orçamento.")
        else:
            print("\nDespesas dentro do limite permitido.")
    except:
        opcao_invalida()

def main():
    os.system("cls")
    analise_do_orcamento()

def opcao_invalida():
    print("\nOpção invalida, digite apenas números inteiros ou decimais. \n")
    input("Pressione qualquer tecla para continuar...\n")
    main()

if __name__ == "__main__":
    main()
