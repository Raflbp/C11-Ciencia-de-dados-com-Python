import numpy as np

dataset = np.loadtxt(r'C:\Users\Rafael Bruno\Desktop\Rafael\Faculdade\Inatel\6º Periodo\C11\C11-Ciencia-de-dados-com-Python\Cap_4_Paises\paises.csv'
, delimiter = ';', dtype = str)

Nth_coutry = np.char.upper(dataset[1: , 1])

mascara_paises = np.char.find(Nth_coutry , 'NORTHERN AMERICA') >= 0

Qtn_Nth = np.sum(mascara_paises)

print(Qtn_Nth)