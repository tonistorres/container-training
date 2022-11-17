"""
2 - Funções de criação de array 2D
As funções de criação de matrizes 2D, por exemplo numpy.eye, numpy.diag, e numpy.
vander definem propriedades de matrizes especiais representadas como matrizes 2D.

np.eye(n, m)define uma matriz de identidade 2D. Os elementos em que i=j
(índice de linha e índice de coluna são iguais) são 1 e os demais são 0, assim:
"""
# https://www.youtube.com/watch?v=EzOjhjFfM-w
import numpy as np

array_1 = np.eye(3, dtype=int)
print("Array 1:\n", array_1)

# define a linha diagonal de 1(uns)
array_2 = np.eye(4, k=-1)
print("Array 2:\n", array_2)
array_2_1 = np.eye(5, k=2)
print("Array 2.1:\n", array_2_1)

array_3 = np.eye(3, 5)
print("Array 3:\n", array_3)
