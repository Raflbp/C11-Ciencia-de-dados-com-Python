import numpy as np

# 1. Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# 2. Isola a coluna de empresas 
empresas = dataset[1:, 1]

nomes_unicos, contagens = np.unique(empresas, return_counts=True)

for i in range(len(nomes_unicos)):
    print(f"Empresa: {nomes_unicos[i]} | Quantidade de missões: {contagens[i]}")