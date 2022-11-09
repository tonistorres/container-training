# Subtração
# A subtract()função subtrai os valores de uma matriz
#  com os valores de outra matriz e retorna os resultados
#  em uma nova matriz.

# Exemplo
# Subtraia os valores em arr2 dos valores em arr1:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)
