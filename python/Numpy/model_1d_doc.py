# https://www.w3schools.com/python/numpy/numpy_array_indexing.asp
import numpy as np

a = np.array([2, 3, 4])


print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{a}
2- Qual Tipo do Array:{type(a)}
3- Número de Linhas e Colunas do Array:{a.shape} e Nº Dimenssões:{a.ndim}
4- Qual Tipo de elementos contidos nesse Array:{a.dtype}
5- Número de Elementos contidos na Matriz:{a.size}
-----------------------------------------------
Access Array Elements
-----------------------------------------------
6- Acessando primeiro elemento numa matriz a unidimensional:{a[0]}
7- Acessando último elemento numa matriz a unidimensional:{a[-1]}
8- Faça uma ADIÇÃO entre o PRIMEIRO e o ÚLTIMO elemento da matriz:{a[0]+a[-1]}
"""
)
