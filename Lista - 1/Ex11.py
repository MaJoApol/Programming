'''
Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
ao final mostrar seu nome e salário final calculado.
'''
nome = input("Insira seu nome: ")
horas = int(input("Número de horas trabalhadas: "))
valor = float(input("Valor da hora trabalhada: "))
bruto = horas * valor

print(f"{nome}, seu salário bruto é de: R${bruto:.2f}")
print(f"{nome}, seu salário descontado é de: R${bruto - (bruto * 0.02):.2f}")
