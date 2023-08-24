'''
Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre
os itens repetidos. 
'''
esporte = ["GR", "Futebol", "Vôlei", "Tênis", "Basquete", "GR", "Vôlei"]

for i in esporte:
    if esporte.count(i) > 1:
        print(i)