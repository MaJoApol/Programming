'''
Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.
'''
p = 0

jogos = ["Tomb Raider", "Minecraft", "God of War", "Moonlighter", "GTA V"]
print(jogos)

elemento = input("Que jogo você quer procurar na lista? \n")

if elemento in jogos:
    print(f"\nO jogo {elemento} está na posição {jogos.index(elemento)}")
