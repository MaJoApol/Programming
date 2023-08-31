'''
 Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.
'''

from random import randint

vitoria = 0

while True:
    pi = input("Par [P] ou Impar [I]: ").upper()
    comp = randint(0, 10)
    val = int(input("Digite um valor: "))
    if pi == "P":
        if (comp + val) % 2 == 0:
            print("Você venceu!")
            vitoria += 1
        else:
            print("Você perdeu!")
            break
    elif pi == "I":
        if (comp + val) % 2 == 0:
            print("Você Perdeu!")
            break
        else:
            print("Você Venceu!")
            vitoria += 1


