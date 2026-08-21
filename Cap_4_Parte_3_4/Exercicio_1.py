import numpy as np

# 1. Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

status_missao = np.char.upper(dataset[1:, 7])

porcentagem_sucesso = np.mean(status_missao == 'SUCCESS') * 100

print(f"{porcentagem_sucesso:.2f}%")