##Exercicio 5
Numero = int(input("Digite um número entre 1000 e 9999: "))

while Numero < 1000 or Numero > 9999:
    print("Número inválido")
    Numero = int(input("Digite um número entre 1000 e 9999: "))

print("Numero: ", Numero)
print("Dezenas: ", Numero // 10 % 10)
print("Centenas: ", Numero // 100 % 10)
print("Milhar: ", Numero // 1000 % 10)