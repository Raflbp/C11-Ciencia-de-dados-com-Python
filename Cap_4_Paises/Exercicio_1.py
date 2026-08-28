import numpy as np
# Faça um slicing no dataset para mostrar apenas o Pais (Country), Região
# (Region), População (Population) e Area (Area (sq. mi.)) dos paises contidos
# nele;


dataset = np.loadtxt(
    'paises.csv',
    delimiter=';',
    dtype=str
)

dados = dataset[0:, 0:4]

print(dados)