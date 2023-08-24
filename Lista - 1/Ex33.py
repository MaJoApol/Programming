'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. A percentagem de votos nulos sobre o total de votos;
'''
total = 0

jose = []
mario = []
carla = []
marilia = []
nulo = []

control = int(input("""Você deseja votar?
 (1) - SIM
 (0) - NÃO 
 R: """))

if control == 1:
    while control != 0:
        total += 1
        voto = int(input(""" ------------------
     1 - José
     2 - Mario
     3 - Carla
     4 - Marília 
     5 - Nulo
     Insira aqui seu voto: """))
        
        if voto == 1:
            jose.append(voto)
        if voto == 2:
            mario.append(voto)
        if voto == 3:
            carla.append(voto)
        if voto == 4:
            marilia.append(voto)
        if voto == 3:
            nulo.append(voto)

        control = int(input("""Você deseja votar?
 (1) - SIM
 (0) - NÃO 
 R: """)) 



print("------ TOTAL DE VOTOS ------")
print(f"José - {len(jose)}")
print(f"Mario - {len(mario)}")
print(f"Carla - {len(carla)}")
print(f"Marília - {len(marilia)}")
print(f"Nulo - {len(nulo)}")
print(f"Total de votos: {total}")

print("------ PORCENTAGEM DE NULOS------")

print(f"Dos votos contabilizados, {(len(nulo) * 100) / total}")




