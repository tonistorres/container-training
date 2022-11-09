# Multiplicação
# A multiply()função multiplica os valores de uma matriz
# pelos valores de outra matriz e retorna os resultados
# em uma nova matriz.

# Exemplo
# Multiplique os valores em arr1 pelos valores em arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1, arr2)

print(newarr)
