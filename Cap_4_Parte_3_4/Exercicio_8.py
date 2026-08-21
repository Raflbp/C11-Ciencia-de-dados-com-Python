import numpy as np

# 1. Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

empresas = dataset[1:, 1]
gasto = dataset[1:, 6].astype(float)

#Salvo a posição maxima
indice_maximo = np.argmax(gasto)

empresa = empresas[indice_maximo]

valor = gasto[indice_maximo]

print(empresa)
print(valor)