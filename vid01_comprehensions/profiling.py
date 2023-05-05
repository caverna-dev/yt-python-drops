import cProfile

numeros = range(0, 10**8)

# usando for loop
def fnc_for_loop():
    lista_nums = []
    for numero in numeros:
        lista_nums.append(numero + 1)
    return lista_nums


# usado uma list comprehension
def func_comprehension():
    lista_nums = [num + 1 for num in numeros]
    return lista_nums

print("Executando com loop for")
cProfile.run('fnc_for_loop()')

print('*' * 50)

print("Executando com list comprehension")
cProfile.run('func_comprehension()')