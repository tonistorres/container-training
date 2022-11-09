import numpy as np

pares = np.array([n for n in range(0, 101, 2)])
print(pares)


print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{pares}
2- Qual Tipo do Array:{type(pares)}
3- Número de Linhas e Colunas do Array:{pares.shape} e Nº Dimenssões:{pares.ndim}
4- Qual Tipo de elementos contidos nesse Array:{pares.dtype}
5- Número de Elementos contidos na Matriz:{pares.size}
-----------------------------------------------
Access Array Elements
-----------------------------------------------
8- Faça uma ADIÇÃO entre o PRIMEIRO e o ÚLTIMO elemento da matriz:{pares[0]+pares[-1]}
"""
)
