"""
O randommétodo do resultado de default_rngirá
criar um array preenchido com valores aleatórios
entre 0 e 1. Está incluso na numpy.random biblioteca.
Abaixo, são criados dois arrays com formas (2,3)
e (2,3,2), respectivamente. A semente é definida
como 42 para que você possa reproduzir esses números
pseudo-aleatórios
"""
# Do this (new version)
from numpy.random import default_rng

print(default_rng(42).random((2, 3)))
