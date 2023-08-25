'''
Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

'''
n1 = float(input("Insira A1: "))
n2 = float(input("Insira A2: "))
n3 = float(input("Insira A3: "))
media = (n1 + n2 + n3) / 3

if media >= 6:
    print(f"Aprovado, sua média é {media:.2f}")
else:
    print(f"Reprovado, sua média é {media:.2f}")

