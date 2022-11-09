import numpy as np

l = [
    [88, 19, 46, 74, 94],
    [8, 9, 6, 4, 4],
    [8, 1, 4, 7, 9],
    [888, 198, 468, 748, 948],
    [889, 199, 469, 749, 949],
]
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
Para resolvermos essa problemática temos que ter a percepção e lermos
o fatiamento da seguite forma:
a --> O array em questão
[] --> Símbolo que representa o fatiamento quando pos-posto ao array
1:3 --> entenda esse primerio slicing/fatiamento como sendo:
      a) 1 --> Linha;
      b) 3 --> Linha, sendo que o fatiamento irá ocorrer de fato
               até o índice 2, pois, o três por definição do python
               não entra na contagem quando efetuado slicing, é como se
               fosse n-1, ou seja, 3-1=2 então só vai até o dois.

1:4 --> entenda esse segundo fatiamento como sendo:
      a) 1 --> Coluna;
      b) Até 4-> Ou melhor dizendo só irá até a 3 por definição do python

Fatiar a Matriz 2d a[1:3,1:4]={a[1:3,1:4]}
"""
)
