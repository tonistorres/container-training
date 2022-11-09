"""
Crie um array 3D com dois arrays 2D, ambos contendo dois arrays
com os valores 1,2,3 e 4,5,6:

"""
import numpy as np

# array tridimenssional
arr = np.array(
    [
        [[9, 20, 33], [40, 50, 60]],  # dimenssão 0 / bloco 0
        [[1, 2, 3], [4, 5, 6]],  # dimenssão 1 / bloco 1
        [[25, 26, 28], [24, 23, 88]],  # dimenssão 2 / bloco 2
        [[100, 102, 105], [555, 654, 1002]],  # dimenssão 3 / bloco 3
    ]
)
print(arr)
print(arr[1][1][2])
