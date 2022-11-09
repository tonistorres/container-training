# Fatiamento Negativo
# Use o operador menos para se referir a um índice
#  a partir do final:

# Exemplo
# Fatia do índice 3 do final para o índice 1 do final:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(f"Fatia do índice 3 (final) ao 1(final):\n{arr[-3:-1]}")
