"""
Um erro frequente consiste em chamar arraycom vários argumentos,
em vez de fornecer uma única sequência como argumento.

"""
import numpy as np


def handling_frequent_error():
    try:
        a = np.array(1, 2, 3, 4)
    except TypeError:
        print(f"Foma correta de criar a matriz seria: a = np.array([1, 2, 3, 4]")


handling_frequent_error()
