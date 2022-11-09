# # Poder
# A power()função eleva os valores da primeira matriz
#  à potência dos valores da segunda matriz e retorna
#  os resultados em uma nova matriz.

# Exemplo
# Eleve os valores em arr1 à potência dos valores em arr2:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)
