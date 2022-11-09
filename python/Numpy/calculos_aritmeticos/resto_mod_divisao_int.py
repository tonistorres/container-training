# Restante
# As funções mod()the e the remainder()retornam o
# restante dos valores na primeira matriz correspondentes
# aos valores na segunda matriz e retornam os resultados
# em uma nova matriz.

# Exemplo
# Devolva os restos:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.mod(arr1, arr2)

print(newarr)
