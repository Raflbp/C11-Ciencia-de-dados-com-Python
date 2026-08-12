lista_produtos = []

for i in range(3):
    Nome = input("Nome do produto: ")
    Preco = float(input("Preço do produto: "))
    Quantidade_Produto = int(input("Quantidade do produto: "))

    produto_atual = {
        'nome': Nome,
        'preco': Preco,
        'quantidade': Quantidade_Produto
    }

    lista_produtos.append(produto_atual)


for produto in lista_produtos:
    print(produto['nome'])
    print(produto['preco'] * produto['quantidade'])
