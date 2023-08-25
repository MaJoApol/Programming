'''
Leia a idade e o tempo de servicço de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

'''
age = int(input("Insira sua idade: "))
servico = int(input("Anos de serviço: "))

if age >= 65:
    print("Aposentadoria aprovada.")
elif servico >= 30:
    print("Aposentadoria aprovada.")
elif age >= 60 and servico >= 25:
    print("Aposentadoria aprovada.")
else:
    print("Aposentadoria reprovada.")