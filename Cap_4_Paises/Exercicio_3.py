import numpy as np

dataset = np.loadtxt(r'C:\Users\Rafael Bruno\Desktop\Rafael\Faculdade\Inatel\6º Periodo\C11\C11-Ciencia-de-dados-com-Python\Cap_4_Paises\paises.csv',
                    delimiter=';' ,
                    dtype=str
                    )

Alfabetizacao = dataset[1: ,9].astype(float)

Med_alfabe = np.mean(Alfabetizacao)


print(f'{Med_alfabe:.2f}')