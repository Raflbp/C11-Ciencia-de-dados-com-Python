import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# EXERCÍCIOS (PARTE 4)
# ==========================================

# Carregar o dataset paises.csv
paises = pd.read_csv('paises.csv', sep=';')

# Limpeza e conversão das colunas de texto com vírgulas para formato numérico
colunas_interesse = ["GDP ($ per capita)", "Literacy (%)", "Infant mortality (per 1000 births)", "Phones (per 1000)"]
for col in colunas_interesse:
    if col in paises.columns and paises[col].dtype == 'object':
        paises[col] = paises[col].str.replace(',', '.').astype(float)

# 5. Correlação entre indicadores socioeconómicos em Heatmap
plt.figure(figsize=(8, 6))
corr_paises = paises[colunas_interesse].corr()
sns.heatmap(corr_paises, annot=True, cmap='viridis', fmt=".2f")
plt.title('5. Correlação de Indicadores Socioeconómicos')
plt.show()

# 6. Boxplot de GDP comparando América Latina e Europa Ocidental
plt.figure(figsize=(8, 5))
# Filtrar as duas regiões pretendidas
regioes_alvo = ['LATIN AMER. & CARIB', 'WESTERN EUROPE']
paises_filtrados = paises[paises['Region'].str.strip().isin(regioes_alvo)]

sns.boxplot(data=paises_filtrados, x='Region', y='GDP ($ per capita)')
plt.title('6. Distribuição do GDP per capita: América Latina vs Europa Ocidental')
plt.xticks(rotation=10)
plt.show()

# 7. Regplot: Taxa de Alfabetização vs Mortalidade Infantil
plt.figure(figsize=(8, 5))
sns.regplot(data=paises, x='Literacy (%)', y='Infant mortality (per 1000 births)',
            line_kws={"color": "orange"})
plt.title('7. Regplot: Alfabetização vs Mortalidade Infantil')
plt.show()

# 8. Dataset space.csv - Boxplot de custo de missões por status do foguete
space = pd.read_csv('space.csv', sep=';')

# Tratamento da coluna Cost caso venha como string com vírgulas
if ' Cost' in space.columns and space[' Cost'].dtype == 'object':
    space[' Cost'] = space[' Cost'].str.replace(',', '').astype(float)
elif 'Cost' in space.columns and space['Cost'].dtype == 'object':
    space['Cost'] = space['Cost'].str.replace(',', '').astype(float)

# Utilizar o nome exato da coluna de custo e status (verifique os espaços no nome das colunas)
col_custo = ' Cost' if ' Cost' in space.columns else 'Cost'
col_status = 'Status Rocket' if 'Status Rocket' in space.columns else 'StatusRocket'

# Filtrar custos > 0 e os status pedidos
space_filtrado = space[(space[col_custo] > 0) & (space[col_status].isin(['StatusActive', 'StatusRetired']))]

plt.figure(figsize=(8, 5))
sns.boxplot(data=space_filtrado, x=col_status, y=col_custo)
plt.title('8. Distribuição do Custo das Missões por Status do Foguete')
plt.show()()