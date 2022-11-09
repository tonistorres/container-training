import numpy as np

dim = (2, 3)

a = np.random.random(dim)


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
