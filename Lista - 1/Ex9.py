'''
Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros.
'''

nome = input("Insira seu nome: ")
reais = float(input("Insira a quantia em reais: R$"))


print(f"Conversão para dólares em nome de {nome}: {reais * 0.18:.2f}")
print(f"Conversão para euros em nome de {nome}:{reais * 0.19:.2f}")