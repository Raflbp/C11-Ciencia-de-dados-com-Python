#Criando um dicionário
Pessoa = {}

#Quantidade de pessoas
Quantidade_de_Pessoas = int(input("Digite a quantidade de pessoas: " ))

#Entrada de dados das pessoas
for i in range(Quantidade_de_Pessoas):
    Nome = input("Nome da pessoa: ")
    Idade = int(input("Idade da pessoa: "))
    Sexo = input("Sexo da pessoa (M/F): ")
    Pessoa[Nome] = (Idade, Sexo)

# A)
#Media de idade
media_idade = int(sum(Pessoa[nome][0] for nome in Pessoa) / Quantidade_de_Pessoas)

#Mostrar a média de idade
print("Média de idade: ", media_idade)

# B)
Quantidade_de_Mulheres = 0

for nome in Pessoa:
    if Pessoa[nome][1] == "F" and Pessoa[nome][0] > 20:
        Quantidade_de_Mulheres += 1

print("Quantidade de mulheres: ", Quantidade_de_Mulheres)