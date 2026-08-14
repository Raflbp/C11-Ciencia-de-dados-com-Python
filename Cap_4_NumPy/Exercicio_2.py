import numpy as np


array_0_51 = np.arange(0, 52, 2) 
Array_100_50 = np.arange(100,48,-2)

Array_concatenado = np.concatenate((array_0_51 , Array_100_50))

print(np.sort(Array_concatenado))
