import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Tipo o zero representa as duas dimensões aqui representadas
# O 1º dois depois do zero representa a dimensão 0
# O 2º dois depois do zero representa a dimensão 1
print(arr[0:1, 1])  # para mim deveria retornar 2 e 7
print(arr[0:2, 2])
print(arr[0:3, 3])
print(arr[0:4, 4])

"""
Retorno

[2]
[3 8]
[4 9]
[ 5 10]


"""
