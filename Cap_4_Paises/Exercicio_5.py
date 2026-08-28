import numpy as np

dataset = np.loadtxt('paises.csv',delimiter=';',dtype=str)

coutry_gdp = np.char.upper(dataset[1:, [0, 1, 8]])

mask_ctygdp = np.char.find(coutry_gdp[:, 1],'LATIN AMER. & CARIB') >= 0

gdp = coutry_gdp[mask_ctygdp][:, 2].astype(float)

Max_gdp = np.max(gdp)

print(Max_gdp)