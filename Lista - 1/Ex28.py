'''
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato
'''

total = 0

mario = []
carla = []
marilia = []


control = int(input("""Você deseja votar?
 (1) - SIM
 (0) - NÃO 
 R: """))

if control == 1:
    while control != 0:
        total += 1
        voto = int(input(""" ------------------
     1 - Mario
     2 - Carla
     3 - Marília 
     Insira aqui seu voto: """))

        if voto == 1:
            mario.append(voto)
        if voto == 2:
            carla.append(voto)
        if voto == 3:
            marilia.append(voto)
        control = int(input("""Você deseja votar?
 (1) - SIM
 (0) - NÃO 
 R: """))



print("------ TOTAL DE VOTOS ------")
print(f"Mario - {len(mario)}")
print(f"Carla - {len(carla)}")
print(f"Marília - {len(marilia)}")
print(f"Total de votos: {total}")

