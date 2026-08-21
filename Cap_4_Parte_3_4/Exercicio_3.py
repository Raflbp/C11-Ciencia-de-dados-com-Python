import numpy as np

# 1. Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

#Separando coluna no dataset
coluna = np.char.count(dataset[1:, 2], 'USA')

print(np.sum(coluna))