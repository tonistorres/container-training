import numpy as np

# matriz identidade é uma matriz quadrada
# logo para ser criada só precisa de um inteiro

n = 4
a = np.eye(n, dtype=int)


print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{a}
2- Número de Linhas e Colunas do Array:{a.shape} e Nº Dimenssões:{a.ndim}
3- Qual Tipo do Array:{type(a)}
4- Qual Tipo de elementos contidos nesse Array:{a.dtype}
5- Número de Elementos contidos na Matriz:{a.size}
"""
)
