# https://www.youtube.com/watch?v=Dw2TdjgCJeo
# Criar um array 3d(lista de três dimenssões)
# Para setar um elemento x num array 3d basta seguir a seguinte
# Fórmula:
# [0] --> define qual bloco você irá trabalhar dentro do array tridimenssional
# [1] --> define a linha que você irá setar dentro do bloco escolhido
# [2]--> define a coluna que você irá setar dentro do bloco escolhido
# Sitaxe: array[0][1][2]
import numpy as np

cubo = np.array([[[1, 4, 7], [3, 5, 2], [5, 6, 0]], [[7, 4, 1], [2, 8, 8], [0, 3, 6]]])

print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{cubo}
2- Qual Tipo do Array:{type(cubo)}
3- Número de Linhas e Colunas do Array:{cubo.shape} e Nº Dimenssões:{cubo.ndim}
4- Qual Tipo de elementos contidos nesse Array:{cubo.dtype}
5- Número de Elementos contidos na Matriz:{cubo.size}
6- Acesse o elemento ZERO do 1º BLOCO array 3d:{cubo[0][2][2]}

"""
)

# Pecorrendo um array tridimenssional
for i in range(2):  # primeiro define o numero de blocos
    for j in range(3):  # segundo define o numero de linhas
        for k in range(3):  # terceiro define o numero de colunas
            print("Posição {0},{1},{2}:{3}".format(i, j, k, cubo[i][j][k]))
