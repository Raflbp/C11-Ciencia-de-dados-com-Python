import numpy as np


Matriz = np.array([[10,20],[30,40]])
linhas_colunas = Matriz.shape[0] * Matriz.shape[1]

print(Matriz)
print(Matriz.shape[0] * Matriz.shape[1])

if (linhas_colunas % 2 == 0):
    print('Par')
else:
    print('impar')
