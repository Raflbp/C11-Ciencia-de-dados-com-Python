import numpy as np
import pandas as pd

# lista de labels(Colunas)
colunas = ['W', 'X', 'Y', 'Z']

# lista de labels(Linhas)
linhas = ['A', 'B', 'C', 'D', 'E']

np.random.seed(10)
valores = np.random.randint(1, 50 , [5,4])

df = pd.DataFrame(columns=colunas, 
                    index=linhas,
                    data = valores)


#Exercicio 1
#Salvando valores menores que 30 em uma variável
Menor_30 = valores[valores < 30]

#Calculando a média dos valores menores que 30
media = (Menor_30.mean())

print(f'{media:.2f}')

#Exercicio 2
#Calculando a media  linha D
Media_D = (df.loc['D'].mean())

#Somando os elementos da linha E iloc
Soma_E = (df.iloc[4].sum())

print(f'{Media_D:.2f}')
print(f'{Soma_E:.2f}')


#Exercicio 3
#Slicing linhas A,C e E e colunas X e Y
print(df.loc[['A','C','E'],['X','Y']])

