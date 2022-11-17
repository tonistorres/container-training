"""
------------------------------------------------------
numpy.diag
entorpecido. diag ( v , k = 0 )[fonte]
Extraia uma diagonal ou construa uma matriz diagonal.
------------------------------------------------------
pode definir uma matriz 2D quadrada com valores
fornecidos ao longo da diagonal ou , se for fornecida uma
matriz 2D, retorna uma matriz 1D que é apenas os elementos
diagonais. As duas funções de criação de matriz podem ser
úteis ao fazer álgebra linear, como:
"""
import numpy as np

array_diag_1 = np.diag([1, 2, 3])
print("Array diag 1:\n", array_diag_1)

# criar uma matriz x com 9 elementos
# utilizando método arange e moldando seu reshape
# para uma matriz dimensional 3x3
x = np.arange(9).reshape((3, 3))
print("Array x:\n", x)

result = np.diag(x)
print("O capturar a Diagonal:\n", result)

capture_position_1 = np.diag(x, k=1)
print("Capture os elementos da diagona na posição k=1:\n", capture_position_1)


capture_position_2 = np.diag(x, k=-1)
print("Capture os elementos da diagona na posição k=-1:\n", capture_position_2)
