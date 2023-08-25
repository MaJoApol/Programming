'''
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 * h) - 58
• Mulheres: (62, 1 * h) - 44, 7

'''
sexo = input("""Masculino - [M]
Feminino - [F]
--> """).upper()
h = float(input("Sua altura:"))

if sexo == "M":
    print(f"Seu peso ideal é: {(72.7 * h) - 58:.2f}")
elif sexo == "F":
    print(f"Seu peso ideal é: {(62.1 * h) - 44.7:.2f}")


