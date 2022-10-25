"""
2. Altere o código da atividade 1 para que ele exiba
os números múltiplos de 2, 5 e 7 e que
"""

# declaração das variáveis
inicio = 100
fim = 500
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim + 1):
    if (numero % 2 == 0) and (numero % 5 == 0) and numero % 7 == 0:
        print(numero)
