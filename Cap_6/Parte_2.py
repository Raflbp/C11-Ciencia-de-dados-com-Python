import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os datasets
ds_paises = pd.read_csv('paises.csv', sep=';')
ds_space = pd.read_csv('space.csv', sep=';')

# 5.
df_latam = ds_paises[ds_paises['Region'].str.contains('LATIN AMER', na=False)]
print("--- Países da América Latina ---")
print(df_latam[['Country', 'GDP ($ per capita)', 'Literacy (%)', 'Population']].head())

tamanhos = df_latam['Population'] / 200000 

plt.figure(figsize=(8, 5))
plt.scatter(df_latam['GDP ($ per capita)'], df_latam['Literacy (%)'], s=tamanhos, alpha=0.5, color='green')
plt.title('Renda per capita vs Alfabetização (América Latina)')
plt.xlabel('GDP ($ per capita)')
plt.ylabel('Literacy (%)')
plt.show()

# 6. 

df_rocket_status = ds_space[ds_space['Status Rocket'].isin(['StatusActive', 'StatusRetired'])]
rocket_status = df_rocket_status['Status Rocket'].value_counts()

print("\n--- Status dos Foguetes ---")
print(rocket_status)

plt.figure(figsize=(6, 6))
plt.pie(x=rocket_status.values, labels=rocket_status.index, autopct='%1.1f%%', colors=['skyblue', 'gray'])
plt.title('Status Geral dos Foguetes')
plt.show()


# 7.

df_we = ds_paises[ds_paises['Region'].str.contains('WESTERN EUROPE', na=False)]

print("\n--- Países da Europa Ocidental ---")
print(df_we[['Country', 'GDP ($ per capita)', 'Phones (per 1000)']].head())

plt.figure(figsize=(10, 5))
plt.plot(df_we['Country'], df_we['GDP ($ per capita)'], 'o-b', linewidth=2, markersize=6, label='GDP ($ per capita)')
plt.plot(df_we['Country'], df_we['Phones (per 1000)'], 's--r', linewidth=2, markersize=6, label='Phones (per 1000)')

plt.title('GDP vs Telefones na Europa Ocidental')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()


# 8.

top_5_success = ds_space[ds_space['Status Mission'] == 'Success']['Company Name'].value_counts().head(5)
top_5_fail = ds_space[ds_space['Status Mission'] == 'Failure']['Company Name'].value_counts().head(5)

print("\n--- Top 5 Sucesso ---")
print(top_5_success)
print("\n--- Top 5 Falha ---")
print(top_5_fail)

plt.figure(figsize=(12, 5))

# Gráfico 1
plt.subplot(1, 2, 1) 
plt.bar(top_5_success.index, top_5_success.values, color='green')
plt.title('Top 5 - Missões de Sucesso')
plt.xticks(rotation=45)

# Gráfico 2
plt.subplot(1, 2, 2) 
plt.bar(top_5_fail.index, top_5_fail.values, color='red')
plt.title('Top 5 - Missões com Falha')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()