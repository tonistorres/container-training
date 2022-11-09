# Valores absolutos
# Ambas as funções absolute()e as abs()funções fazem
# a mesma operação absoluta em termos de elemento,
# mas devemos usar absolute() para evitar confusão
# com o python embutidomath.abs()

# Exemplo
# Retorne o quociente e mod:

import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)
