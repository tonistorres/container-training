import numpy as np

x_min = 5
x_max = 15
a = np.linspace(start=x_min, stop=x_max, num=6, dtype=int)


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
