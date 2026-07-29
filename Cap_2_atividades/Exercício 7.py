
palavra = input("Digite uma palavra: ")

quantidade_vogais = 0
Letra_A = False
vogais = "AEIOU" 

print("Letras da palavra:")

for letra in palavra:

    letra_maiuscula = letra.upper()
    print(letra_maiuscula)
    
    if letra_maiuscula in vogais:
        quantidade_vogais += 1
        
    if letra_maiuscula == 'A':
        Letra_A = True


print("Quantidade de vogais:", quantidade_vogais)

if Letra_A:
    print("A letra 'A' está presente na palavra!")
else:
    print("A letra 'A' NÃO está presente na palavra.")