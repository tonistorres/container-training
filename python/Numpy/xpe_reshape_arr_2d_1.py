import numpy as np


# slicing em array 2D (matrizes)
# criando uma matriz com 6 elementos
a = np.arange(10)

print(
    f"""-----------------------------------------------
   Criado Array 10 Elementos Método arange
-----------------------------------------------
"""
)
print(a)
# que possui 2 dimensões defindas abaixo
# 3 - linhas;
# 2 - colunas

print(
    f"""-----------------------------------------------
   Redefinindo a forma dessa matriz unidimensional
   Método reshape (2,5)
-----------------------------------------------
"""
)
x = a.reshape((2, 5))
print(x)

print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
1- Número de Linhas e Colunas do Array:{x.shape} e Nº Dimenssões:{x.ndim}
2- Número de Elementos contidos na Matriz:{x.size}
3- Acessando Primeira LINHA Segunda COLUNA:{x[0,1]}
4- Acessando Segunda LINHA Penúltima COLUNA:{x[1,-2]}
5- Acessando Ultima LINHA Última COLUNA:{x[-1,-1]}
6- Acessando Ultima LINHA Última COLUNA:{x[1,4]}
7- Acessando Primeira LINHA inteira:\n{x[0, :]}
8- Acessando Primeira LINHA Segunda até Quarta COLUNA:\n{x[0,1:4]}
9- Acessando Todas as LINHAS Segunda até Quarta COLUNA:\n{x[:,[1,2,3,4]]}
10-Acessando Apenas a Ultima coluna de Ambas as Linhas:\n{x[:,[-1]]}
"""
)
