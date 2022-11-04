# https://www.youtube.com/watch?v=LidaJMcVmu4
"""
Bosion Treinamentos

"""

import numpy as np

numeros = np.array([1, 2, 3, 4, 5], np.int16)

print(numeros)
print(numeros[4])
print(type(numeros))
# tipo dos dados
print(numeros.dtype)
# modificando numeros no array
numeros[0] = 5
print(numeros)
