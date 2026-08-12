Bolo = {'Ovos', 'Farinha', 'Açúcar', 'Fermento', 'Leite', 'Manteiga', 'Chocolates', 'Baunilha'}

Ingredientes_pessoa1 = {'Ovos', 'Farinha', 'Açúcar', 'Leite'}
Ingredientes_pessoa2 = {'Fermento', 'Manteiga'}

Existentes = Ingredientes_pessoa1 | Ingredientes_pessoa2

Faltantes = Bolo - Existentes

print(Faltantes)
