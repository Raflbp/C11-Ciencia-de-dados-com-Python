import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# EXERCÍCIOS (PARTE 3)
# ==========================================

# 1. Dataset Iris - Correlação para a espécie 'setosa'
iris = sns.load_dataset('iris')
setosa = iris[iris['species'] == 'setosa']
corr_setosa = setosa.select_dtypes(include=['number']).corr()

plt.figure(figsize=(6, 4))
sns.heatmap(corr_setosa, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('1. Correlação entre variáveis numéricas - Espécie Setosa')
plt.show()

# 2. Dataset Titanic - Distribuição de idades por sexo com curva de densidade (KDE)
titanic = sns.load_dataset('titanic')

plt.figure(figsize=(8, 5))
sns.histplot(data=titanic, x='age', hue='sex', kde=True, bins=30, alpha=0.5)
plt.title('2. Distribuição das Idades dos Passageiros por Sexo (com KDE)')
plt.show()

# 3. Dataset Titanic - Distribuição de idades em função da classe, segmentado por sexo (Boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(data=titanic, x='class', y='age', hue='sex')
plt.title('3. Distribuição de Idades por Classe e Sexo')
plt.show()

# 4. Dataset mpg - Relação entre potência e consumo de combustível
mpg = sns.load_dataset('mpg')

plt.figure(figsize=(8, 5))
sns.scatterplot(data=mpg, x='horsepower', y='mpg', alpha=0.6)
# Adicionando uma linha de tendência básica (pode-se usar sns.regplot também)
sns.regplot(data=mpg, x='horsepower', y='mpg', scatter=False, color='red')
plt.title('4. Relação entre Potência (horsepower) e Consumo (mpg)')
plt.show()

