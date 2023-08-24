'''
Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²
'''
h = float(input("Altura: "))
l = float(input("Largura: "))
a = h * l

print(f"Sua parede tem {a:.0f}m², para pinta-la será necessário {a / 2:.0f}L de tinta")