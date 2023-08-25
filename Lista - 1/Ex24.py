'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
'''


num = int(input("Digite um número entre 1 e 10: "))

while num < 1 or num > 10:
        print("Número inválido")
        num = int(input("Digite um número entre 1 e 10: "))
