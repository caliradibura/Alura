# Autor: Carlos Lira
# Data: 02/11/2026

import os

def aprovando_emprestimo():
    try:
        renda_mensal = float(input("Digite o valor da sua renda mensal R$: "))
        parcela_desejada = float(input("Digite o valor da parcela desejada R$: "))

        if (renda_mensal < 0) or (parcela_desejada < 0):
            opcao_invalida()
        elif renda_mensal <= 2000:
            print("\nEmprestimo negado: renda mensal tem que ser maior que R$ 2000,00")
        else:
            parcela_em_porcentagem = (parcela_desejada/renda_mensal) * 100
            if parcela_em_porcentagem > 30:
                print(f"\nEmprestimo negado: parcela não pode ultrapassar 30%. Parcela atual: {parcela_em_porcentagem:.2f}%")
            else:
                print(f"\nEmprestimo aprovado: parcela equivalente a {parcela_em_porcentagem:.2f}% da renda mensal")
            
    except:
        opcao_invalida()

def opcao_invalida():
    print("\nOpção invalida. Digite um valor positivo\n")
    input("Digite qualquer tecla para continuar... ")
    main()

def main():
    os.system("cls")
    aprovando_emprestimo()

if __name__ == "__main__":
    main()