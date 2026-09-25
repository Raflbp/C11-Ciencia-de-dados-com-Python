import pandas as pd
import numpy as np

# Carregar o dataset
ds = pd.read_csv('paises.csv', sep=';')

# Tratar espaços extras no início e fim dos textos das colunas do tipo string
ds['Region'] = ds['Region'].str.strip()
ds['Country'] = ds['Country'].str.strip()


estatisticas_populacao = ds.groupby('Region')['Population'].describe()

print(estatisticas_populacao.head(5))




# Exercício 7

def reduzir_mortalidade_infantil(valor):
    return valor * 0.85

mortalidade_reduzida = ds['Infant mortality (per 1000 births)'].apply(reduzir_mortalidade_infantil)
mortalidade_reduzida.name = 'Target Infant mortality (-15%)' # Nomeando para a visualização

comparacao = pd.concat([ds['Infant mortality (per 1000 births)'], mortalidade_reduzida], axis=1)

print(comparacao.head(10))




# Exercício 8

ds_sem_coastline = ds.drop(columns=['Coastline (coast/area ratio)'])
ds_sem_coastline.to_csv('paises_sem_coastline.csv', index=False, sep=';')
