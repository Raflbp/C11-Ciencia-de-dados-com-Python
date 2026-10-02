import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os datasets
ds_paises = pd.read_csv('paises.csv', sep=';')
ds_space = pd.read_csv('space.csv', sep=';')


df_na = ds_paises[ds_paises['Region'].str.contains('NORTHERN AMERICA', na=False)]
print(df_na[['Country', 'Deathrate', 'Birthrate']])

plt.figure(figsize=(8, 5))
plt.plot(df_na['Country'], df_na['Deathrate'], 'o-r', linewidth=2, markersize=8, label='Taxa de Mortalidade')
plt.plot(df_na['Country'], df_na['Birthrate'], 's--b', linewidth=2, markersize=8, label='Taxa de Natalidade')

plt.title('Natalidade vs Mortalidade - América do Norte')
plt.xlabel('País')
plt.ylabel('Taxa')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2.
usa_companies = ds_space[ds_space['Location'].str.contains('USA', na=False)]['Company Name'].nunique()
china_companies = ds_space[ds_space['Location'].str.contains('China', na=False)]['Company Name'].nunique()

print(f"\nEmpresas EUA: {usa_companies} | Empresas China: {china_companies}")

plt.figure(figsize=(6, 5))
plt.bar(['EUA', 'China'], [usa_companies, china_companies], color=['blue', 'red'])
plt.title('Número de Empresas Espaciais Únicas')
plt.ylabel('Quantidade de Empresas')
plt.show()


# 3. 

df_roscosmos = ds_space[ds_space['Company Name'] == 'Roscosmos']
status_counts = df_roscosmos['Status Mission'].value_counts()

print("\n--- Status das Missões Roscosmos ---")
print(status_counts)

plt.figure(figsize=(6, 6))
plt.pie(x=status_counts.values, labels=status_counts.index, autopct='%1.1f%%')
plt.title('Status das Missões - Roscosmos')
plt.show()


# 4. 

df_failures = ds_space[ds_space['Status Mission'] == 'Failure']
top_5_failures = df_failures['Company Name'].value_counts().head(5)

print("\n--- Top 5 Empresas com Mais Falhas ---")
print(top_5_failures)

plt.figure(figsize=(8, 5))
plt.bar(top_5_failures.index, top_5_failures.values, color='orange')
plt.title('Top 5 Empresas com Mais Falhas nas Missões')
plt.xlabel('Empresa')
plt.ylabel('Número de Falhas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()