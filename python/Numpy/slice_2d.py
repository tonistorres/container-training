# Fatiando matrizes 2-D
# Exemplo
# Do segundo elemento, corte os elementos do
#  índice 1 ao índice 4 (não incluído):

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# primeiro argumento define o bloco/linha
# segundo argumento define a faixa fatiamento
print(arr[1, 1:4])
