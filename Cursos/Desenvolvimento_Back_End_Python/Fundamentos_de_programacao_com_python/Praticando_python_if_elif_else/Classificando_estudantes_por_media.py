# Autor: Carlos Lira
# Data: 01/11/2026

import os

def coletar_notas():
    try:
        notas = []
        for nota in range(1, 4):
            nota = float(input(f"Digite a nota {nota}: "))
            if nota < 0 or nota > 10:
                os.system("cls")
                print("\nNota inválida! Digite uma nota entre 0 e 10.")
                return coletar_notas()
            notas.append(nota)
        return notas

    except:
        os.system("cls")
        print("Erro ao coletar notas, digite apenas números inteiros ou decimais.")
        return coletar_notas()

def analise_das_notas():
    media = sum(coletar_notas())/3

    if media >= 7:
        print(f"Sua média foi {media:.1f}, você está aprovado")
    elif media < 5:
        print(f"Sua média foi {media:.1f}, você está reprovado")
    else:
        print(f"Sua média foi {media:.1f}, você está em recuperação")

def main():
    analise_das_notas()

if __name__ == "__main__":
    main()