vendas = [
    {"produto": "Notebook", "valor": 3500, "vendedor": "Ana"},
    {"produto": "Mouse", "valor": 80, "vendedor": "Carlos"},
    {"produto": "Teclado", "valor": 150, "vendedor": "Ana"},
    {"produto": "Monitor", "valor": 900, "vendedor": "Carlos"},
    {"produto": "Notebook", "valor": 4000, "vendedor": "João"},
    {"produto": "Mouse", "valor": 100, "vendedor": "Ana"},
]

#execio 01
# total = 0
# for i in range(len(vendas)):
#     total += vendas[i]["valor"]

# print(total)
#execicio 02
# vendedores = {}

# for venda in vendas:
#     nome = venda["vendedor"]
#     valor = venda["valor"]

#     if nome not in vendedores:
#      vendedores[nome] = 0

#     vendedores[nome] += valor

# for nome, total in vendedores.items():
#     print(nome, "vendeu:", total)