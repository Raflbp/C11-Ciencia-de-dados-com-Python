import numpy as np

# Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Isola a coluna
localizacao = np.char.upper(dataset[1:, 2])

mascara_russia = np.char.find(localizacao, 'RUSSIA') != -1

qtd_Russia = np.sum(mascara_russia)

print(f"{qtd_Russia:.2f} ")