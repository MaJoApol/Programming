''' 
Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte.'''

filmes = ["Interestellar", "A cinco passos de você", "Lorax", "Garfield", "Barbie", "Interestellar", "Lorax"]
jogos = ["Moonlighter", "Tomb Raider", "GTA V", "Minecraft", "God of War", "Moonlighter", "GTA V"]
livros = ["Cai o pano", "HeartStopper", "1984", "O extraodinário", "Diario de um banana", "1984", "Cai o pano"]
esportes = ["GR", "Futebol", "Vôlei", "Tênis", "Basquete", "GR", "Vôlei"]

# ---------------------------------------------

print(filmes)
print(jogos)
print(livros)
print(esportes)

#Adicionando -----------------------------------

filmes.append(input("Adicione um filme: "))
jogos.append(input("Adicione um jogo: "))
livros.append(input("Adicione um livro: "))
esportes.append(input("Adicione um esporte: "))

print(filmes)
print(jogos)
print(livros)
print(esportes)

#Uma lista com as 4 listas anteriores -----------------------------------

lazeres = [filmes + jogos + livros + esportes]

print(lazeres)

#Mostrar itens da lista -----------------------------------

books = int(input("Mostre alguns livros de posição 0 até [i]: "))
print(livros[0:books])

#Remova um item da lista esporte ----------------------------
sports = input("Consulte a lista delete um esporte: ")
esportes.remove(sports)
print(esportes)



