# Funções 14/09
#São blocos de código que executam funcionalidades específicas

""" ------ SINTAXE -------
 
 def nomedaFuncao():
    o que sera executado por ela

 """
print("""-------------------------------------------
 
 """)

""" def inicio():
    print("Olá Mundo / Hello word")

inicio()

def flores():
    flor = input("Diga o nome de uma flor:")
    cor = input("Diga o nome de uma cor: ")
    print(f"A sua flor {flor}, tem a cor {cor}")

flores()

# ----PARAMETROS-----------------------------------------------------------------------------

def name(n):
    print("-" * 30)
    print(f"Olá {n} seja bem vindo(a)!")
    print("-" * 30) 

name("Mariane")
name("Chris")
name("Marcos")
#error() -> precisa de paramEtros


def somar(a,b):
    s = a + b
    print(f"Soma entre {a} e {b} é {s}")

somar(9, 8)
somar(1, 7)

# ----EMPACOTAMENTO-----------------------------------------------------------------------------

def somar(*n):
    somar = sum(n)
    size = len(n)
    print(f"Os valores são {n} soma dos valores: {somar}. Tamaho é {size}")
    for i in n:
        print(i)

somar(9, 8, 5, 4, 5)
somar(1, 7)
somar(2)


def somar(a,b):
    s = a + b
    return s

a = somar(1, 7)
print(a)                 --> Variavel agora é trabalhavel


# ---- INPUT -----------------------------------------------------------------------------
def somar(a,b):
    s = a + b
    return s

n = int(input("A: "))
c = int(input("B: "))
a = somar(n, c)
print(a)       

# ---- TRUE / FALSE -----------------------------------------------------------------------------

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

print(par(3))
print(par(2))
print(par(0))


# ---- 2 RETURNS  -----------------------------------------------------------------------------

def somar(a,b):
    s = a + b
    m = a * b
    return s, m

a = somar(1, 7)
print(a)         
print(f"A soma dos valores é {a[0]}") 
print(f"A soma dos valores é {a[1]}") 


# ---- 2 RETURNS Variaveis diferentes --------------------------------------->

def nomeage():
    n = (input("Nome: "))
    i = int(input("Idade: "))
    return n, i

print("Iniciando cadastro....")
nome, idade = nomeage()
print("Cadastro realizado....")
print(f"Você se chama {nome}, e tem {idade} anos de idade")
"""
# ---- Exercício CALCULADORA  -----------------------------------------------------------------------------


def soma(a,b):
    s = a + b
    return s

def sub(a,b):
    s = a - b
    return s

def mult(a,b):
    s = a * b
    return s

def div(a,b):
    s = a / b
    return s

def menu():
    print("Bem Vindo a calculadora!\n")

    while True:
        print("""     1 - SOMA
    2 - SUBTRAÇÃO
    3 - MULTIPLICAÇÃO
    4 - DIVISÃO
    5 - SAIR
        """)

        choice = int(input("Escolha: "))
            
        if choice == 5:
            print("Tchau, tchau...")
            break

        a = float(input("Número um: "))
        b = float(input("Número dois: "))

        if choice == 1:
            calc = soma(a,b)
            print(calc)
        
        if choice == 2:
            calc = sub(a,b)
            print(calc)

        if choice == 3:
            calc = mult(a,b)
            print(calc)

        if choice == 4:
            calc = div(a,b)
            print(calc)

menu()


print("""-------------------------------------------""")