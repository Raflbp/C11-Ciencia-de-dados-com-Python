import numpy as numpy
import pandas as pd

#Exercicio 1 
seriesAn01 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAn02 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

#Exercicio 2
#Somando porcentagem de uso das linguagens 
Usoano1 = seriesAn01.sum()
Usoano2 = seriesAn02.sum()

print(f'Quantidade de uso de Java,C e Python no ano 1: {Usoano1:.2f}')
print(f'Quantidade de uso de Java,C e Python no ano 2: {Usoano2:.2f}')

#Exercicio 3
Growth_Decline = seriesAn02 - seriesAn01
print(Growth_Decline)

#Exercicio 4
print(Growth_Decline[Growth_Decline > 0]) #Crescimento  

#Exercicio 5
#Mantendo as porcentagem pro mais 2 anos
DobroAno1 = seriesAn01 * 2
DobroAno2 = seriesAn02 * 2

Most_use = DobroAno1 + DobroAno2
print( Most_use.nlargest(1))