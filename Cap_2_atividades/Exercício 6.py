## Exercício 6
Numero_decimal = float(input("Digite um número decimal: "))

Raiz_quadrada = Numero_decimal ** 0.5
Funcao_teto = int(Raiz_quadrada) + 1 if Raiz_quadrada % 1 != 0 else int(Raiz_quadrada)
Funcao_piso = int(Raiz_quadrada)
Parte_inteira = int(Numero_decimal)

print("Raiz quadrada:", Raiz_quadrada)
print("Função teto:", Funcao_teto)
print("Função piso:", Funcao_piso)
print("Parte inteira:", Parte_inteira)