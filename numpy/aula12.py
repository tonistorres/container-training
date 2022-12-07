# métodos para criação de array
# https://www.youtube.com/watch?v=uGH_WBEeHag&list=PL3Fmwz_E1hXRWxIkP843DiDf0ZeqgftTy&index=15
import numpy as np

# arange
# array_com_100_numeros_inteiros = np.arange(0, 101)
# print(array_com_100_numeros_inteiros)

# array_com_100_numeros_inteiros_passo_2 = np.arange(0, 101, 2)
# print(array_com_100_numeros_inteiros_passo_2)

# linspace
# A função linspace() retorna números uniformemente espaçados
# em um intervalo especificado [start, stop, step].
# O ponto final do intervalo pode opcionalmente ser excluído.

# criar_array_linspace = np.linspace(1, 10, 10)


# Biblioteca:Numpy -->> Módulo: Random --> Funções--> rand, randn e randint

# Função rand --> cria números aleatorios em 0 e 1
result_rand = np.random.rand(10)
print(result_rand)
print("-------------------------")
result_randn = np.random.randn(10)
print(result_rand)
print("-------------------------")
result_randint = np.random.randint(10, 100, 30)
print(result_randint)
print("Quantos Elementos:", len(result_randint))
print("-------------------------")

# criando array de zeros 2d
result_zeros = np.zeros((5, 2))
print(f"Criando Array com Zeros Valores:\n{result_zeros}")
print("-------------------------")
# criando array de uns 2d
result_um = np.ones((2, 3))
print(f"Criando Array com Ones Valores:\n{result_um}")
