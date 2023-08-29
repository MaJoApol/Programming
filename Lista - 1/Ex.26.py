'''
 Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''


nome = input("Nome: ")
age = int(input("Idade: "))
sal = float(input("Salário: "))
sex = input("F ou M: ").upper()
estcivil = input("""Estado civil:
S - solteiro(a)
C - casado(a)
V - viuvo(a)
D - divorciado(a)
-> """).upper()

if len(nome) > 3:
    print("a. nome, maior que 3 caracteres - True")
else:
    print("a. nome, maior que 3 caracteres - False")

if 0 < age < 150:
    print("b. idade, entre 0 e 150 - True")
else:
    print("b. idade, entre 0 e 150 - False")

if sal > 0:
    print("c. salário, maior que zero - True")
else:
    print("c. salário, maior que zero - False")

if "F" == sex or sex == "M":
    print("d. sexo, 'F' ou 'M' - True")
else:
    print("d. sexo, 'F' ou 'M' - False")

if  estcivil == "S"  or estcivil == "C" or estcivil == "V" or estcivil == "D":
    print("e. estado Civil: 'S', 'C', 'V', 'D' - True")
else:
    print("e. estado Civil: 'S', 'C', 'V', 'D' - False")
