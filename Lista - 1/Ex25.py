
'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


'''
login =[]

name = input("Nome de usuario: ")
senha = input("Senha: ")

while name == senha:
    print("Senha e nome precisam ser diferentes!")
    name = input("Nome de usuario: ")
    senha = input("Senha: ")


