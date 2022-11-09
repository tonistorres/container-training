import numpy as np

# visivel mente temos uma matriz/ndArray 2d
# que consiste em uma matriz 2x2
lista = [[1, 2], [3, 4]]

X = np.array(lista)
print("ANTES modificar array valor X:\n", X)
# O SUB_ARRAY - foi tirado de toda linha do bloco 1 ou
# dimensão 1 do array representado no slice pela posição
# 0 (ZERO). Como não foi definido nem posição inicial e
# nem posição final no segundo argumento do fatiamento então
# está implicito que é a linha toda
SUB_ARRAY = X[0, :]
print("Sub-Array criado a partir do Slice:\n", SUB_ARRAY)
Y = SUB_ARRAY
# a partir do SUB_ARRAY [1 2] eu estou agora pegando
# a segunda posição do SUB_ARRAY 1(um) e atribuindo
# minha variável Y na posição 1 o valor de 10
# o que irá modificar automagicamente o ndArray
# X que não deveria ter nada haver com a operação
# aqui efetuada, se não fosse o simples fato que
# que o slice compartilha a mesma posição de memória
# do array original daí mesmo criando uma varivel para
# fazer essa alteração a mesma reflete no array inicial
# em nosso caso X
Y[1] = 10
print("X:\n", X)
