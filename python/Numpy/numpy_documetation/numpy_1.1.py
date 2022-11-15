"""
1 - Funções de criação de array 1D
As funções de criação de array 1D,
 por exemplo, numpy.linspacee numpy.
 arangegeralmente precisam de pelo
 menos duas entradas, starte stop.

numpy.arangecria arrays com valores
incrementados regularmente. Verifique
a documentação para obter informações
completas e exemplos. Alguns exemplos
são mostrados:
Observação: a melhor prática para numpy.arange
é usar valores de início, fim e etapa inteiros.
Existem algumas sutilezas em relação ao dtype.
No segundo exemplo, o dtypeé definido.
No terceiro exemplo, a matriz dtype=float
deve acomodar o tamanho da etapa de 0.1. Devido
ao erro de arredondamento, o stopvalor às vezes
é incluído.
"""
import numpy as np
import module_head as mh

array_1d = np.arange(10)
mh.head("/", "Criando Array 1D\n    com método arange")
print("Método arange:\n", array_1d)

# start - 2
# stop - 10
# Os valores são gerados dentro do intervalo
# semiaberto
# dtype= float
mh.head("/", "Criando Array 1D\n    com método arange\n    start=2 stop=10 dtype=float")
array_1d_start_stop = np.arange(2, 10, dtype=float)
print("Método arange start stop dtype:\n", array_1d_start_stop)

mh.head("/", "Criando Array 1D\n    com método arange\n    start=2 stop=3 step=0.1")
# start = 2
# stop = 3
# step = 0.1
# um step / passo de 1 décimo no intervalor demarcado pelos argumentos por start e stop
array_3 = np.arange(2, 3, 0.1)
print(array_3)
