# criando um array bidimencional
import numpy as np

numero_bidimensional = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(numero_bidimensional)
print(type(numero_bidimensional))
print(f"Numero de dimenssões:{numero_bidimensional.ndim}")
# acessando elementos no array bidimensional as duas formas possíveis no python
print(numero_bidimensional[0][0])
print(numero_bidimensional[0, 0])
