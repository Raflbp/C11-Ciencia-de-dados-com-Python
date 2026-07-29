##Atividade 3
sexo = input("Digite seu sexo (M/F): ").upper()

while sexo not in ["M", "F"]:
    print("Entrada inválida")
    sexo = input("Digite seu sexo (M/F): ").upper()

if sexo == "M":
    print("Masculino")
else:
    print("Feminino")
