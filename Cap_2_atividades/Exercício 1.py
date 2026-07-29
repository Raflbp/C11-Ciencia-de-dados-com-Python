##Atividade 1   

# Entrada do nome 
nome = input("Digite seu nome completo: ")

# Nome em letras minúsculas e maiúsculas e quantidade de letras
print(nome.lower())
print(nome.upper())
print(len(nome))

#Separando o nome em partes e substituindo o último sobrenome por "do Inatel"
nome_parte = nome.split()
nome_parte[-1] = "do Inatel"
novo_nome = " ".join(nome_parte)
print(novo_nome)
