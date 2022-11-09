import numpy as np

# Bem esse trecho de código estoura um erro
# de indexação o que é totalmente compreensível
# quando observamos o array de 1D onde temos apenas
# as posições: 0=1., 1=1., 2=1.,3=0. e 4=NÃO EXISTE
TRECHO_ERRADO = np.ones((4,))
TRECHO_ERRADO[4] = 0.0
print(TRECHO_ERRADO)


# Este Resulta
D = np.zeros((4,))
D[:-1] = 1.0
print(D)


# Este Resulta
Y = np.ones((4,))
Y[-1] = 0.0
print(Y)


Z = np.zeros((4,))
Z[:3] = 1.0
print(Z)
