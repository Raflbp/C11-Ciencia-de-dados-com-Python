#Criação do dicionario
aluno = {}

#Entrada do nome e media
nome = input("nome do aluno: ")
media = float(input("Media do aluno: ")) 

#Atribuição dos valores ao dicionario
aluno["Nome"] = nome
aluno["Media"] = media

#Verificação da situação do aluno
if media >= 50:
    aluno["Situacao"] = "AP"
else:
    aluno["Situacao"] = "RP"

#Mostrando conteudo do dicionario
print(aluno)