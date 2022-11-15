"""
numpy.linspace criará arrays com um número especificado de elementos
e espaçados igualmente entre os valores iniciais e finais especificados.
A vantagem desta função de criação é que você garante o número de elementos
e o ponto inicial e final.
O anterior não incluirá o valor .arange(start, stop, step)stop
"""
import numpy as np
import module_head as mh

array_test = np.linspace(1.0, 4.0, 6)
mh.head("/", "Criando ndArray \n    start=1. stop=4.0 num=6 ")
print(array_test)
