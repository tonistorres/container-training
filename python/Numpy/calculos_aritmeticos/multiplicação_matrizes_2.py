import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

result = np.dot(arr1, arr2)
print(f"Resultado da Multiplicação:\n{result}")
print(f"Resultado da Multiplicação:\n{arr1.dot(arr2)}")
