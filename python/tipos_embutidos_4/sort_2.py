# https://www.youtube.com/watch?v=TVXEIDO3D2g
"""
utilizando o sort agente faz a ordenação no proprio array
é melhor gerar um novo array ordenado do que mexer no array
base ...
"""

from pprint import pprint

data1 = [3, 1, 4, 7, 2]
data2 = [3, 1, 4, 7, 2]

data1.sort(reverse=True)
data2.sort()
pprint(f"sort Crescente { data2}")
pprint(f"sort Reverse {data1}")
