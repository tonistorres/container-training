"""
As funções de criação de ndarray, por exemplo numpy.ones,
numpy.zeros, e random definem matrizes com base na forma desejada.
As funções de criação de ndarray podem criar arrays com qualquer
dimensão especificando quantas dimensões e comprimento ao longo
dessa dimensão em uma tupla ou lista.

numpy.zeroscriará uma matriz preenchida com 0 valores com a forma
especificada. O dtype padrão é float64:

"""

import numpy as np
import module_head as mh

# criando um array de zeros 1D de 5 Elementos

arr_1D_5El = np.zeros(5, dtype=int)
mh.head("/", "Criando uma matriz\n    1D com 5 Elementos")
print("Matriz 1D com 5 Elementos:\n", arr_1D_5El)

arr_2D_6El = np.zeros((2, 3))
mh.head("/", "Criando uma matriz\n    2D com 6 Elementos")
print("Matriz 2D com 6 Elementos:\n", arr_2D_6El)

arr_3D_20El = np.zeros((4, 5, 3))
# 4 - Representa o Nº de Blocos/dimensão da Matriz
# 5 - Representa numero de Linhas da Matriz
# 3 - Representa o numero de Colunas da Matriz
mh.head("/", "Criando uma matriz\n    3D com 20 Elementos")
print("Matriz 3D com 12 Elementos:\n", arr_3D_20El)
