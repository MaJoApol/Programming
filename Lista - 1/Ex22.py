'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada.
'''

valor = []
num = 0

while num != 1000:
    num = int(input("Insira um número: "))
    valor.append(num)

valor.pop()
print(len(valor))
print(sum(valor))
