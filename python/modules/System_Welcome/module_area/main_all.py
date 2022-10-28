"""
Posso importar todas funções contidas no meu módulo
calculator_area.py
para isso observe o exemplo abaixo
"""

from calculator_area.calculator import *

result = area_triangle_lambda()
print(result(10, 20))


result_2 = area_rectangle(5, 5)
print(result_2)
