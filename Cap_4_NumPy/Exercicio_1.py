import numpy as np

array1 = np.ones([8])
array2 = np.random.randint(0,9,8)
array3 = array2 + array1

array_soma = np.sum(array1 + array2)

print(array_soma)

if array_soma >= 40:
    array_remodelado = array3.reshape(4, 2)
else:
    array_remodelado = array3.reshape(2, 4)

print(array_remodelado)