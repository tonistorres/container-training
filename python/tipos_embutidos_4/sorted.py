"""
Neste caso iremos gerar um novo array ordenado
a partir do array base o que é mais interessante
"""

from pprint import pprint

data1 = [3, 1, 4, 7, 2]
data2 = [3, 1, 4, 7, 2]
data1_sorted = sorted(data1)
data2_sorted = sorted(data2, reverse=True)
pprint(data1_sorted)
pprint(data2_sorted)
