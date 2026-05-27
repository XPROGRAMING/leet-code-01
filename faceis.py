# maior numero
# nums = [4, 7, 1, 9, 3]
# maior = 0
# for valor in nums:
#     if valor > maior:
#         maior = valor
# print(maior)

# menor numero
# nums = [4, 7, 1, 9, 3]
# menor = nums[0]
# for i in nums:
#     if i < menor:
#         menor = i
# print(menor)

# soma tudo
# nums = [4, 7, 1, 9, 3]
# soma = 0

# for i in nums:
#     soma += i

# print(soma)

nums = [100, 4, 200, 1, 3, 2]
nums_set = set(nums)
maior = 0

for num in nums_set:
    if num - 1 not in nums_set:
        tamanho = 1
        while num + tamanho in nums_set:
            tamanho += 1
        if tamanho > maior:
            maior = tamanho
print(maior)