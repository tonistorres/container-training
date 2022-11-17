""""
numpy.onescriará uma matriz preenchida com 1 valores.
É idêntico a zerosem todos os outros aspectos como tal:
"""
import numpy as np


arr_2D_6El = np.ones((2, 3))
# 2 - Representa o Numero de Linhas da Matriz
# 3 - Representa o Numero de Colunas da Matriz
print("Array shape 2,3 :\n", arr_2D_6El)

arr_3D_12El = np.ones((2, 3, 2))
# 2 - Representa o Numero de Blocos / Dimesão
# 3 - Representa o Numero de Linhas da Matriz
# 4 - Representa o Número de Colunas da Matriz

print("Array shape 2,3,2: \n", arr_3D_12El)
