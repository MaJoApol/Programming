'''
Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 números.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero).

'''
opcao = int(input("""Soma de 2 números - [1]
Diferença entre 2 números (maior pelo menor) - [2]
Produto entre 2 números - [3]
Divisão entre 2 números (o denominador não pode ser zero) - [4]
Sair - [0]
--> """))

while opcao != 0:
    if opcao == 1:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        print(f"{n1} + {n2} = {n1+n2}")
        opcao = int(input("""--------------------------------
Soma de 2 números - [1]
Diferença entre 2 números (maior pelo menor) - [2]
Produto entre 2 números - [3]
Divisão entre 2 números (o denominador não pode ser zero) - [4]
Sair - [0]
--> """))

    elif opcao == 2:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        if n1 > n2:
            print(f"{n1} - {n2} = {n1-n2}")
        else:
            print(f"{n2} - {n1} = {n2-n1}")
        opcao = int(input("""--------------------------------
Soma de 2 números - [1]
Diferença entre 2 números (maior pelo menor) - [2]
Produto entre 2 números - [3]
Divisão entre 2 números (o denominador não pode ser zero) - [4]
Sair - [0]
--> """))
        
    elif opcao == 3:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        print(f"{n1} x {n2} = {n1*n2}")
        opcao = int(input("""--------------------------------
Soma de 2 números - [1]
Diferença entre 2 números (maior pelo menor) - [2]
Produto entre 2 números - [3]
Divisão entre 2 números (o denominador não pode ser zero) - [4]
Sair - [0]
--> """))
    
    elif opcao == 4:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        while n2 == 0:
            print("0 não pode ser denominador")
            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))
        print(f"{n1} ÷ {n2} = {n1 / n2}")
        opcao = int(input("""--------------------------------
Soma de 2 números - [1]
Diferença entre 2 números (maior pelo menor) - [2]
Produto entre 2 números - [3]
Divisão entre 2 números (o denominador não pode ser zero) - [4]
Sair - [0]
--> """))
    elif opcao != 0:
        print("Opção inválida")
        opcao = int(input("""--------------------------------
Soma de 2 números - [1]
Diferença entre 2 números (maior pelo menor) - [2]
Produto entre 2 números - [3]
Divisão entre 2 números (o denominador não pode ser zero) - [4]
Sair - [0]
--> """))



