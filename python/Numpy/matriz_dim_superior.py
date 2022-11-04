"""
Matrizes Dimensionais Superiores
Uma matriz pode ter qualquer número de dimensões.
Quando a matriz é criada, você pode definir o número de
dimensões usando o ndminargumento.
"""
# Crie uma matriz com 5 dimensões e verifique se ela possui 5 dimensões:
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print("number of dimensions :", arr.ndim)
