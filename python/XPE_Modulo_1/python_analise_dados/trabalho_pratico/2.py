import numpy as np

# função zeros()
# A função zeros() é usada para obter uma nova matriz de determinada
# forma e tipo, preenchida com zeros.
# Essa notação omitindo o  valor da coluna (4 Linha, x Coluna) curiosamente
# cria um numpy array contendo 1(uma) Linha com 4 Colunas preenchidas com zeros
# (float/ponto flutuante)

z = np.zeros((4,))
print("Array Resultante ANTES:\n", z)
# Observação: Nesse ponto fazemos uma atribuição
# na segunda posição do ndArray, sim segunda posição
# pois, levando em consideração que a contagem dos índices
# de um ndarray inicia no zero a posição 1 é a segunda posição
z[1] = 1
# Com a atribuição feita na posição 1 do array
# abaixo iremos imprimir na tela com o comando
# pirnt a matriz original alterada na posição 1
print("Array Resultante DEPOIS:\n", z)
