# https://www.w3schools.com/python/numpy/numpy_array_indexing.asp
"""
ndarray.ndim
o número de eixos (dimensões) da matriz.
"""

import numpy as np

# criando uma matriz de 15 elementos
# com 3 LIHAS e 5 COLUNAS
a = np.arange(15).reshape(3, 5)

print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{a}
2- Qual Tipo do Array:{type(a)}
3- Número de Linhas e Colunas do Array:{a.shape} e Nº Dimenssões:{a.ndim}
4- Qual Tipo de elementos contidos nesse Array:{a.dtype}
5- Número de Elementos contidos na Matriz:{a.size}
6- Verificar a PRIMEIRA COLUNA da matriz:{a[:,0]}
7- Verificar a SEGUNDA COLUNA da matriz:{a[:,1]}
8- Verificar a TERCEIRA COLUNA da matriz:{a[:,2]}
9- Acesse o Elemento na PRIMEIRA LINHA e SEGUNDA COLUNA:{a[0,1]}
10-Acesse o Elemento da SEGUNDA LINHA e QUARTA COLUNA:{a[1,4]}
"""
)
