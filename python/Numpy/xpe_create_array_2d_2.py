import numpy as np

l = [[1, 2], [3, 4]]

a = np.array(l)

print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Imprimindo o Array:\n{a}
2- Número de Linhas e Colunas do Array:{a.shape} e Nº Dimenssões:{a.ndim}
3- Qual Tipo do Array:{type(a)}
4- Qual Tipo de elementos contidos nesse Array:{a.dtype}
5- Número de Elementos contidos na Matriz:{a.size}
6- Acesse o Elemento na PRIMEIRA LINHA e SEGUNDA COLUNA:{a[0,0]}
7- Acesse o Elemento da SEGUNDA LINHA e QUARTA COLUNA:{a[1,1]}
8- Soma dos Elementos do Item 6 e 7:{a[0,0]+a[1,1]}
"""
)
