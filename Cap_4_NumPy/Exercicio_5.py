import numpy as np

np.random.seed(10)

Matriz = np.random.randint(1, 51, size=(4, 4))

Media_linha = np.mean(Matriz, axis=1)
Media_coluna = np.mean(Matriz, axis=0)

Max_media_linha = np.max(Media_linha)
Max_media_colunas = np.max(Media_coluna)


valores, contagens = np.unique(Matriz, return_counts=True)
Aparicoes = (valores, contagens)

Aparicoes_2_vezes = valores[contagens == 2]



print(Media_coluna)


print(Media_linha)
print('---------------')

print(Max_media_colunas)
print('---------------')

print(Max_media_linha)
print('---------------')

print(valores,contagens)
print('---------------')

print(Aparicoes_2_vezes)
    