# Quociente e Mod
# A divmod()função retorna o quociente e o mod.
#  O valor de retorno são dois arrays, o primeiro
#   array contém o quociente e o segundo array contém o mod.

# Exemplo
# Retorne o quociente e mod:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)
