numeros = [2, 4, 6, 8, 10]

# OBJETIVO 1: obter uma lista contendo cada numero em 'numeros' somado de 1

# usando for loop
lista_nums_for = []
for numero in numeros:
    lista_nums_for.append(numero + 1)

# usado uma list comprehension
lista_nums_comp = [numero + 1 for numero in numeros]


# OBJETIVO 2: obter um dicionário em que cada cada chave é um numero em 'numeros' e cada valor é o quadrado do numero
# em questão
dict_for = {}
for numero in numeros:
    dict_for[numero] = numero*numero

dict_comp = {numero: numero*numero for numero in numeros}



# OBJETIVO 3: obter um set contendo a potencia de numero elevado a si mesmo, para cada numer em 'numeros'
set_nums = {num**num for num in numeros}
# print(set_nums)
# print(type(set_nums))



# OBJETIVO 4: obter uma tuple contendo cada numero em 'numeros' somado de 1
nao_funciona_para_tuplas = (num + 1 for num in numeros) # isto nao eh uma comprehension, mas sim um GENERATOR
print(nao_funciona_para_tuplas)
print(type(nao_funciona_para_tuplas))









