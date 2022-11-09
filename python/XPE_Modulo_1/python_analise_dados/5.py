import numpy as np

A = np.ones((2, 2))
print("Resultado de A:\n", A)

B = np.ones((2, 2))
print("Resultado de B:\n", B)

X = A + B

# aqui temos o resultado a soma das duas matrizes
print(f"O resultado da Soma das Duas Matrizes:\n{X}")


Y = np.array([2.0] * 4)
print("Antes reshape:\n", Y)
Z = np.array([2.0] * 4).reshape(2, 2)
print("Depois resahpe:\n", Z)


W = 2 * np.ones((2, 2))
print("Resultado Matriz 2x2 de ones multiplicado por 2", W)


H = np.twos((2, 2))

print("Essa errada", H)
