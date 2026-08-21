import numpy as np

# Importa o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Isola a coluna de status do foguete 
status_rocket = dataset[1:, 5]

# Conta quantidade de missões
total_missoes = len(status_rocket)

# Cria a máscara para 'StatusRetired' e soma quantos deram Verdadeiro 
qtd_aposentados = np.sum(status_rocket == 'StatusRetired')

# Calcula a porcentagem 
porcentagem = (qtd_aposentados / total_missoes) * 100

print(f"{porcentagem:.2f} %")