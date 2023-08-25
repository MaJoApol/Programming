'''
Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
tela dizendo se está “quente”, “frio” ou “agradável”.
'''

temp = float(input("Digite a temperatura: "))

if temp <= 20:
    print("Frio")
elif  20 < temp < 27:
    print("Agradável")
else:
    print("Quente")

