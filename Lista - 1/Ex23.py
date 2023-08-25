'''
Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores.
'''


valor = []
print("""Ler números - [S]
Parar - [N]""")

control = input("--> ").upper()

while control == "S":
    valor.append(int(input("Insira um número: ")))
    control = input("Continuar? --> ").upper()

print(sum(valor) / len(valor))
print(max(valor))
print(min(valor))
