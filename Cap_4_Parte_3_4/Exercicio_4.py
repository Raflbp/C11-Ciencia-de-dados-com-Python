import numpy as np

# 1. Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

#Separando coluna no dataset
empresas = dataset[1:, 1]
gastos = dataset[1:, 6].astype(float)

mascara_spacex = (empresas == 'SpaceX')

gastos_spacex = gastos[mascara_spacex]

valor_mais_caro = np.max(gastos_spacex)

print(valor_mais_caro)