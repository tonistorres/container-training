def multi(valor1, valor2):
    array = []
    i = 0
    while len(array) < valor1:
        i += 1
        array.append(i * valor2)
    return array


result = multi(-3, 7)
print(result)
