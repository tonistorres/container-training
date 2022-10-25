"""
3. Altere o código da atividade 1, criando uma variável divisor e, em seguida, verifique quais os
números no intervalo entre 0 e 1000 (incluindo o 0 e excluindo o 1000) são múltiplos da
variável divisor .
•
Por exemplo, se o valor de divisor for igual a 3, todos os números múltiplos de 3,
dentro do intervalo, deverão ser exibidos (0, 3, 6, 9, ..., 996, 999).

"""
# declaração das variáveis
from __future__ import division


inicio = 0
fim = 1000
divisor = int(input("Digite um inteiro representando um divisor:"))
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % divisor == 0:
        print(numero)
