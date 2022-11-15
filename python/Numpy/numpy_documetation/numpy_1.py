"""
--------------------------------------------------
Convertendo sequências Python para matrizes NumPy
--------------------------------------------------
Arrays NumPy podem ser definidos usando sequências Python, como listas e tuplas.
Listas e tuplas são definidas usando [...]e (...), respectivamente. Listas e tuplas
podem definir a criação do ndarray:
-------------------------------------------------
uma lista de números criará uma matriz 1D,
uma lista de listas criará uma matriz 2D,
outras listas aninhadas criarão matrizes
de dimensões mais altas. Em geral, qualquer
objeto de matriz é chamado de ndarray no NumPy.
"""
import numpy as np
import module_head as mh

a1D = np.array([1, 2, 3, 4])
a2D = np.array([[1, 2], [3, 4]])
a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
mh.head("/", " Imprimindo Matriz a1D")
print("a1D:\n", a1D)
mh.head("/", " Imprimindo Matriz a2D")
print("a2D:\n", a2D)
mh.head("/", " Imprimindo Matriz a3D")
print("a3D:\n", a3D)

"""
Ao usar numpy.arraypara definir um novo array,
você deve considerar o dtype dos elementos no
array, que pode ser especificado explicitamente.
Esse recurso oferece mais controle sobre as estruturas
de dados subjacentes e como os elementos são manipulados
nas funções C/C++. Se você não for cuidadoso com dtype as
atribuições, poderá obter um estouro indesejado, como tal
Um inteiro com sinal de 8 bits representa inteiros de
-128 a 127. Atribuir a int8matriz a inteiros fora desse
intervalo resulta em estouro.
Se você realizar cálculos com incompatibilidade dtypes,
poderá obter resultados indesejados, por exemplo:
"""

a = np.array([127, 128, 129], dtype=np.int8)
mh.head("/", "Obtendo um estouro por \n    incompatibilidade dtype")
print("a:\n", a)


"""
Observe quando você executa operações com dois
arrays do mesmo dtype: uint32, o array resultante
é do mesmo tipo.
"""

a = np.array([2, 3, 4], dtype=np.uint32)
b = np.array([5, 6, 7], dtype=np.uint32)
c_unsigned32 = a - b
mh.head(
    "/",
    "A boa prática de definir \n    os dtypes no momento \n    da criação do ndarray",
)

print("Array Resultante c:\n", c_unsigned32)
