import numpy as np

# os índices no Python vão de 0 a n-1
# onde n é o tamanho da dimensão
# start = onde inicia a construção do array
# stop = onde termina
# num = quantidae de elementos nesse intervalo de tempo
x = np.linspace(start=10, stop=100, num=10, dtype=int)

print(
    f"""-----------------------------------------------
   Analysis ndArray Report Versão Numpy {np.__version__}
-----------------------------------------------
x:\n {x}
1 - shape {x.shape} e Nº Dimenssões:{x.ndim}
2 - Número de Elementos contidos na Matriz:{x.size}
-----------------------------------------------
 Report Sub-Array Extraction 1 D
-----------------------------------------------
3-  Os 2(dois) Primeiro elementos do array:{x[0:2]} # dois é exclusivo
4-  Os 2(dois) Primeiro elementos do array:{x[:2]}  # dois é exclusivo
5-  Os 2(dois) Últimos Elementos do Array:{x[-2,]}

"""
)
