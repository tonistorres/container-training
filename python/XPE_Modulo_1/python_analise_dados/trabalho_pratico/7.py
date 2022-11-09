# # Documentação:
# # https://www.w3schools.com/python/python_ml_mean_median_mode.asp
import numpy as np

# Dissecando o problema:
# Visivelmente temos uma matriz de duas dimensões
list_2d = [[1, 3], [11, 10]]

X = np.array(list_2d)

print("Imprimindo a Lista:\n", X)
# Método mean em Machine Learning é usando para calcular
# a média. Dessa forma em NumPy usamos o método mean()
# para encontrar à média de valores.
value_mean = X[X > np.pi]
print("Valores de X > 3,1415...:\n", value_mean)
print("A média de 11 + 10 =21 /2 = 10.5:\n", np.mean(value_mean))

# O problema como ele é:
# X = np.array([[1, 3], [11, 10]])
# print(np.mean(X[X > np.pi]))
