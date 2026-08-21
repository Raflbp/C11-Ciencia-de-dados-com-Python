import numpy as np

# 1. Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

#Setando a  coluna e qual o tipo de variavel
gastos = dataset[1:, 6].astype(float)

#Somando os gatos maiores que 0
gastos_validos = gastos[gastos > 0]

#faz a media dos gastos
media = np.mean(gastos_validos)

#mostra o valor 
print(f"{media:.2f}")