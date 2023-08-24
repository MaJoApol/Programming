'''
Faça um script que leia algo pelo teclado e mostra na tela o seu tipo de dado.
'''

algo = input("Digite algo: ")

print(type(algo))

# Independente do que digitarmos, o tipo sempre retornara string, isso pois não modificamos covertemos o dado dele antes, por exemplo int(input) ou float(input).S