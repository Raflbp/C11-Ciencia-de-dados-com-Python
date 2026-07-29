##Atividade 4
Distancia = float(input('Digite a distância em Km: '))

if Distancia <= 200:
    Preco = Distancia * 0.50
else:
    Preco = Distancia * 0.45

print(f"O preço da passagem é: R$ {Preco:.2f}")