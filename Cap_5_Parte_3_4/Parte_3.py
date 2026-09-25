import pandas as pd
import numpy as np

# Carregar o dataset
ds = pd.read_csv('paises.csv', sep=';')

# Tratar espaços extras no início e fim dos textos das colunas do tipo string
ds['Region'] = ds['Region'].str.strip()
ds['Country'] = ds['Country'].str.strip()


# Exercício 1

oceania_mask = ds['Region'].str.contains('OCEANIA', case=False, na=False)

# a) Quais são os países da OCEANIA
paises_oceania = ds[oceania_mask]['Country']
print("1.a) Países da OCEANIA:")
print(paises_oceania.to_string(index=False))

# b) Quantos países são da OCEANIA
qtd_oceania = oceania_mask.sum()
print(f"\n1.b) Quantidade de países da OCEANIA: {qtd_oceania}\n")



# Exercício 2

# Encontre o nome e a região do país com maior população[cite: 1]
idx_maior_pop = ds['Population'].idxmax()
pais_maior_pop = ds.loc[idx_maior_pop, ['Country', 'Region']]

print("2) País com maior população e sua região:")
print(f"País: {pais_maior_pop['Country']}, Região: {pais_maior_pop['Region']}\n")



# Exercício 3

# Média de alfabetização (Literacy (%)) por região[cite: 1]
media_alfabetizacao = ds.groupby('Region')['Literacy (%)'].mean()

print(media_alfabetizacao.round(2))



# Exercício 4

sem_costa = ds[ds['Coastline (coast/area ratio)'] == 0][['Country']]
sem_costa.to_csv('noCoast.csv', index=False, sep=';')


# Exercício 5

def classificar_mortalidade(deathrate):
    mapa = {True: 'Balanced', False: 'Urgent'}
    return mapa[deathrate < 9]

ds['Humanitarian Help'] = ds['Deathrate'].apply(classificar_mortalidade)

print(ds[['Country', 'Deathrate', 'Humanitarian Help']].head(10))