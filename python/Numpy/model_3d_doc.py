import numpy as np

a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# https://www.youtube.com/watch?v=Dw2TdjgCJeo

print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{a}
2- Qual Tipo do Array:{type(a)}
3- Número de Linhas e Colunas do Array:{a.shape} e Nº Dimenssões:{a.ndim}
4- Qual Tipo de elementos contidos nesse Array:{a.dtype}
5- Número de Elementos contidos na Matriz:{a.size}

"""
)
