import numpy as np

# Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo
# este dataset;

# Importa o dataset
dataset = np.loadtxt(
    'paises.csv',
    delimiter=';',
    dtype=str
)

# Pega a coluna Região, ignorando o cabeçalho
regioes = dataset[1:, 1]

# Encontra as regiões diferentes e conta
regioes_diferentes = np.unique(regioes)

print("Quantidade de regiões:", len(regioes_diferentes))
print("Regiões:")
print(regioes_diferentes)