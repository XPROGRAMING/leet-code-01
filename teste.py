# exercicio 01
# nums = [10,20,30,40,50]

# soma = 0
# for num in nums:
#     soma += num
# print(soma)


# exercicio 02
# nums = [4,8,1,99,23]

# maior = 0
# for i in nums:
#     if i > maior:
#         maior = i

# print (maior)

# exercicio 03

# nums = [2,5,8,11,14,20]

# par = []
# for num in nums:
#     if num % 2 == 0:
#         par.append(num)

# print(par)

# exercicio 04

# nums = [10,20,30]

# soma = 0
# for num in nums:
#     soma += num

# tamanho = len(nums)
# media = soma / tamanho

# print("A media e: ", media)

# exercicio 05
# nums = [1,1,2,2,3,4,4]

# noduplicatec = []
# for num in nums:
#     if num not in noduplicatec:
#         noduplicatec.append(num)

# print(noduplicatec)

# exercicio 06
# nums = [5,12,7,20,3,15]
# m10 = []

# for num in nums:
#     if num > 10:
#         m10.append(num)

# print(m10)

# exercicio 07
# nums = [1,2,3,4]
# lista_invertida = nums[::-1]

# print(lista_invertida)

# exercicio 08
# palavras = ["python", "java", "python", "c", "java", "python"]
# somatoria = {}

# for palavra in palavras:
#     if palavra not in somatoria:
#         somatoria[palavra] = 0
#     somatoria[palavra] += 1


# print(somatoria)

# exercicio 09

# notas = {
#     "Ana": 8,
#     "Carlos": 10,
#     "João": 7
# }
# maior_nota = 0
# nome01 = ""
# for nome, nota in notas.items():
#     if nota > maior_nota:
#         maior_nota = nota
#         nome01 = nome

# print("A maior nota e do: ", nome01, "que tirou", maior_nota)

# exercicio 10

# gastos = [
#     {"categoria": "comida", "valor": 50},
#     {"categoria": "transporte", "valor": 30},
#     {"categoria": "comida", "valor": 70},
# ]

# soma ={}

# for gasto in gastos:
#     categoria = gasto["categoria"]
#     valor = gasto["valor"]

#     if categoria not in soma:
#         soma[categoria] = 0
#     soma[categoria] += valor

# print(soma)

# exercicio 11
# 11-a. Some as vendas por vendedor
# vendas = [
#     {"vendedor": "Ana", "valor": 300},
#     {"vendedor": "Carlos", "valor": 500},
#     {"vendedor": "Ana", "valor": 700},
#     {"vendedor": "João", "valor": 400},
#     {"vendedor": "Carlos", "valor": 200}
# ]
# somatoria = {}

# for venda in vendas:
#     vendedor = venda["vendedor"]
#     valor = venda["valor"]

#     if vendedor not in somatoria:
#         somatoria[vendedor] = 0
#     somatoria[vendedor] += valor
# print(somatoria)

# 11-b Descubra quem vendeu mais
# vendas = [
#     {"vendedor": "Ana", "valor": 300},
#     {"vendedor": "Carlos", "valor": 500},
#     {"vendedor": "Ana", "valor": 700},
#     {"vendedor": "João", "valor": 400},
#     {"vendedor": "Carlos", "valor": 200}
# ]
# somatoria = {}

# for venda in vendas:
#     vendedor = venda["vendedor"]
#     valor = venda["valor"]

#     if vendedor not in somatoria:
#         somatoria[vendedor] = 0
#     somatoria[vendedor] += valor

# maior_vendedor = 0
# nome01 = ""
# for nome, valor in somatoria.items():
#     if valor > maior_vendedor:
#         maior_vendedor = valor
#         nome01 = nome

# print("o maior vendedor foi: ", nome01, "Que vendeu: ", maior_vendedor)
# exercicio 11-c

# vendas = [
#     {"vendedor": "Ana", "valor": 300},
#     {"vendedor": "Carlos", "valor": 500},
#     {"vendedor": "Ana", "valor": 700},
#     {"vendedor": "João", "valor": 400},
#     {"vendedor": "Carlos", "valor": 200}
# ]

# somatoria = {}
# for venda in vendas:
#     vendedor = venda["vendedor"]
#     valor = venda["valor"]
#     if vendedor not in somatoria:
#         somatoria[vendedor] = 0
#     somatoria[vendedor] += valor

# somatudo = 0
# for nome, valor in somatoria.items():
#     somatudo += valor
# media = somatudo / len(somatoria)

# print("Total vendido:", somatudo)
# print("Media por vendedor:", media)

# two sum

# target = 9
# nums = [11,15,2,7]
# mapa = {}

# for i, num in enumerate(nums):
#     complemento = target - num

#     if complemento in mapa:
#         print([mapa[complemento], i])

#     mapa[num] = i

# nums = [4,8,1,20,3]
# maior = 0

# for i in nums:
#     if i > maior:
#         maior = i

# print(maior)

# frase = "python java python javascript java python"
# frase = frase.split()

# hash = {}

# for palavra in frase:
#     if palavra not in hash:
#         hash[palavra] = 1
#     else:
#         hash[palavra] += 1

# print(hash)

# nums = [4, 5, 1, 2, 5, 4, 3, 2, 2]

# hash = {}
# duplicados = []
# for num in nums:
#     if num not in hash:
#         hash[num] = 1
#     else:
#         hash[num] += 1

# for chave,valor in hash.items():
#         if valor > 1:
#              duplicados.append(chave)
            
# print(duplicados)

# nums = [100, 4, 200, 1, 3, 2]

# nums.sort()

# sequencia_atual = 1
# maior = 1

# for i in range(len(nums)-1):
#     if nums[i] + 1 == nums[i+1]:
#         sequencia_atual += 1
#         if sequencia_atual > maior:
#             maior = sequencia_atual
#     else:
#         sequencia_atual = 1
# print(maior)

# target = 24
# lista = [5,3,23,16,1]

# for i in range(len(lista)):
#     for j in range(len(lista)):
#         soma = lista[i] + lista[j]
#     if soma == target:
#         print([i,j])
# two sum brute force
# lista = [11,15,7,2]
# target = 9

# for i in range(len(lista)):
#     for j in range(len(lista)):
#         soma = lista[i] + lista[j]
#     if soma == target:
#         print([i,j])

# two sum hash map
# target = 9
# nums = [11,2,5,8,2,3,1,7]
# hasher = {}

# for i,num in enumerate(nums):
#     complemento = target - num

#     if complemento in hasher:
#         print(hasher[complemento], i)

#     hasher[num] = i

# nums = [4,8,2,10,3,19,20,30,100]
# maior = 0

# for i in nums:
#     if i > maior:
#         maior = i

# print(f"o maior numero da lista e: {maior}")