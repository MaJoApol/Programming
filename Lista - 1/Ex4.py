'''
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre
ele.
'''
algo = input("Digite algo: ")

print(f"É numerico? {algo.isnumeric()}")
print(f"É string? {algo.isalpha()}")
print(f"É decimal? {algo.isdecimal()}")  #supostamente era ra retornar numeros decimais, mas retorna quando é int, e números decimais ele da falso em todos
print(f"É numerico ou string? {algo.isalnum()}")
print(f"Ta em letra minúscula? {algo.islower()}")
print(f"Ta em leta maiúscula? {algo.isupper()}")
print(f"Começa com letra maiúsula? {algo.istitle()}")
