'''
Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista.
'''
p = 0

jogos = ["Moonlighter", "Tomb Raider", "GTA V", "Minecraft", "God of War", "Moonlighter", "GTA V"]
print(jogos)

elemento = input("Que jogo você quer procurar na lista? \n")

if elemento in jogos:
    for i in jogos:
        while i != elemento:
            p += 1
else:
    print("\nO jogo não está na lista")
print(f"\nO jogo {elemento} está na posição {p}")