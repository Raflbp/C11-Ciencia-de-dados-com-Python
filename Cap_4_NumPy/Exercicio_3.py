import numpy as np

campo_minado = np.zeros([2,2])

linha_aleatoria = np.random.randint(0, 2)
coluna_aleatoria = np.random.randint(0, 2)

campo_minado[linha_aleatoria, coluna_aleatoria] = 1

print(campo_minado)

acertos = 0

while True:
    linha_jogada = int(input("Escolha a linha (0 ou 1): "))
    coluna_jogada = int(input("Escolha a coluna (0 ou 1): "))
    
    if campo_minado[linha_jogada, coluna_jogada] == -1:
            print("Game Over!: Try Again!")
            break
    
    elif campo_minado[linha_jogada, coluna_jogada] == 0:
        campo_minado[linha_jogada, coluna_jogada] = 1
        acertos = acertos + 1
        print("")
    else:
        campo_minado[linha_jogada, coluna_jogada] = 1
        acertos = acertos + 1
        break

    if acertos == 3:
            campo_minado[linha_aleatoria, coluna_aleatoria] = 1
            print("\nCongratulations! You beat the game! :)")
            print(campo_minado)
            break
            
    else:
        print("Você já escolheu esse local! Tente outro.")