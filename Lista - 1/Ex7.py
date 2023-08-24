'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
de aumento.
'''
preco = float(input("Insira o valor do produto: R$"))

print(f"Com acréscimo 15%:  R${preco + (preco * 0.15) }")
print(f"Com decréscimo 5%:  R${preco - (preco * 0.05) }")
