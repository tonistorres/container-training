import numpy as np

# função zeros()
# A função zeros() é usada para obter uma nova matriz de determinada
# forma e tipo, preenchida com zeros.
# Essa notação omitindo o  valor da coluna (4 Linha, x Coluna) curiosamente
# cria um numpy array contendo 1(uma) Linha com 4 Colunas preenchidas com zeros
# (float/ponto flutuante)
z = np.zeros((4,))
print(f"Array Resultante ANTES:\n{z}")
# Neste ponto fazemos um slice a partir da segunda posição do ndArray
# por baixo dos panos o python faz algo tipo um for em todo os elementos
# a partir do índice 1(segundo elemento da matriz) e neste caso ele faz
# atribuição de 1. em todos os elementos a partir do índice 1
z[1:] = 1.0
print(f"Array Resultante DEPOIS:\n{z}")
