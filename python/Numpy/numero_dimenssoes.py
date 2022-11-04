"""
Verificar Número de Dimensões?
NumPy Arrays fornece o ndimatributo que retorna um inteiro
que nos diz quantas dimensões o array possui.
"""

# Verifique quantas dimensões os arrays têm:
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)