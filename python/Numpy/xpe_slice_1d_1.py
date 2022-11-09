import numpy as np

l = [88, 19, 46, 74, 94]
a = np.array(l)


print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{a}
2- Número de Linhas e Colunas do Array:{a.shape} e Nº Dimenssões:{a.ndim}
3- Qual Tipo de elementos contidos nesse Array:{a.dtype}
4- Qual Tipo do Array:{type(a)}
5- Número de Elementos contidos na Matriz:{a.size}
-----------------------------------------------
Access Array Elements
-----------------------------------------------
6- Acessando primeiro elemento numa matriz a unidimensional:{a[0]}
7- Acessando o penúltimo elemento da matriz unidimenssional:{a[-2]}
8- Acessando último elemento numa matriz a unidimensional:{a[-1]}
9- Faça uma ADIÇÃO entre o PRIMEIRO e o ÚLTIMO elemento da matriz:{a[0]+a[-1]}
10-Fatiar o Array da índice 1 ao 3:{a[1:3]}
"""
)
