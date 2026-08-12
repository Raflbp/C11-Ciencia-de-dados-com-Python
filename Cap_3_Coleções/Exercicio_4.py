#Definindo dicionario
Pessoa = {}

#Entrada nome e peso
for i in range(3):
    nome = input("nome da pessoa: ")
    peso = float(input("Peso da pessoa: "))
    Pessoa[nome] = peso

#Verificando a pessoa mais pesada e a mais leve
if len(Pessoa) >= 0:
    print("A pessoa mais pesada é: " + max(Pessoa, key=Pessoa.get))
    print("A pessoa mais leve é: " + min(Pessoa, key=Pessoa.get))
