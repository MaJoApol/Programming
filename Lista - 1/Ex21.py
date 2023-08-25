'''
Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
'''

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
minmax = [n1, n2]

opcao = int(input("""Somar - [1]
Multiplicar - [2]
Maior - [3]
Menor - [4]
Sair - [0]
--> """))

while opcao != 0:
    if opcao == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
        opcao = int(input("""--------------------------------
        Somar - [1]
        Multiplicar - [2]
        Maior - [3]
        Menor - [4]
        Sair - [0]
        --> """))

    elif opcao == 3:
        print(f"Maior: {max(minmax)}")
        opcao = int(input("""--------------------------------
        Somar - [1]
        Multiplicar - [2]
        Maior - [3]
        Menor - [4]
        Sair - [0]
        --> """))


    elif opcao == 2:
        print(f"{n1} x {n2} = {n1 * n2}")
        opcao = int(input("""--------------------------------
        Somar - [1]
        Multiplicar - [2]
        Maior - [3]
        Menor - [4]
        Sair - [0]
        --> """))

    elif opcao == 4:
        print(f"Menor: {min(minmax)}")
        opcao = int(input("""--------------------------------
        Somar - [1]
        Multiplicar - [2]
        Maior - [3]
        Menor - [4]
        Sair - [0]
        --> """))

    elif opcao != 0:
        print("Opção inválida")
        opcao = int(input("""--------------------------------
        Somar - [1]
        Multiplicar - [2]
        Maior - [3]
        Menor - [4]
        Sair - [0]
        --> """))



