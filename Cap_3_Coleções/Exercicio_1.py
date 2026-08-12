#Lista de times do Campeonato
Brasileirao = ['Palmeiras', 'Flamengo', 'Atletico_PR', 'Fluminense', 'Cruzeiro']

#A) Imprimindo os 3 primeiros colocados
print(Brasileirao[0:3])

#B) Imprimindo os 2 últimos colocados
print(Brasileirao[3:5])

#C) Imprimindo os times em ordem alfabética
print(sorted(Brasileirao))

#D) Em que posição se encontra o Barcelona
if 'Barcelona' in Brasileirao:
    posicao = Brasileirao.index('Barcelona') + 1
    print(f'Barcelona está na posição {posicao}.')
else:
    print('O Barcelona não esta na lista')