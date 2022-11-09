# Divisão
# A divide()função divide os valores de um
#  array com os valores de outro array e
#  retorna os resultados em um novo array.

# Exemplo
# Divida os valores em arr1 com os valores em arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)
