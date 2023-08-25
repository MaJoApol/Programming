'''
Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
conversão.
'''

conv = int(input("""Celsius para Fahrenheit - (1)
Fahrenheit para Celsius - (2)
--> """))

if conv == 1:
    cels = float(input("Celsius: "))
    print(f"Fahrenheit: {(cels * (9/5)) + 32}")
elif conv == 2:
    far = float(input("Fahrenheit: "))
    print(f"Celsius: {(far - 32) * 5/9}")
