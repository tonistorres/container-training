# https://numpy.org/doc/stable/user/basics.indexing.html
import numpy as np

x = np.arange(20)
x.shape = (4, 5)

print(f"Imprimindo x:\n{x}")
# primeira posição - representa a linha
# segunda posição  -  representa a coluna
print(f"slice x[1,3]:{x[1,3]}")
# Observação: Num array se eu definir apenas uma posição
# no array ele me retornará toda linha relacionada
# a posição passada.
print(f"slice x[0]: {x[0]}")
# retorne o elemento 19 do array em questão
print(f"Retornado a posição 19:{x[3,-1]}")
