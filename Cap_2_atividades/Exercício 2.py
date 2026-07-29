##Exercicio 2

Tabuada = int(input("Numero para sua tabuada: "))
Tabuada_maxima = int(input("Quantas multiplicações deseja fazer: "))
for i in range(1, Tabuada_maxima + 1):
    resultado = Tabuada * i
    print(f"{Tabuada} x {i} = {resultado}")