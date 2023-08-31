'''
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
'''

codigo = int(input("Código da cidade: "))
veiculo = int(input("Número de veículos de passeio: "))
acidente = int(input("Número de acidentes de trânsito com vítimas: "))

maiorA = acidente
menorA = acidente
codmaior = codigo
codmenor = codigo
totalV = veiculo
totalA = 0


if veiculo < 2000:
    mediaA = acidente

i = 1

while i != 5:
    codigo = int(input("Código da cidade: "))
    veiculo = int(input("Número de veículos de passeio: "))
    acidente = int(input("Número de acidentes de trânsito com vítimas: "))
    totalV += veiculo

    if maiorA < acidente:
        maiorA = acidente
        codmaior = codigo

    if menorA > acidente:
        menorA = acidente
        codmenor = codigo

    if veiculo < 2000:
        totalA = acidente

    i += 1

print(f"Maior índice de acidentes {maiorA} pertence a {codmaior}")
print(f"Menor índice de acidentes {menorA} pertence a {codmenor}")
print(f"Média de veiculos: {totalV / 5}")
print(f"Média de acidentes de trânsito nas cidades com menos de 2.000 veículos: {totalA / 5}")

