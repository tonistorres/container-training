"""
Determine o valor inicial e final do range
Por padrão, o valor inicial do laço de repetição é 0.
Podemos alterar esse valor no comando range.
"""

valor_inicial_range = int(input("Digite o valor inicilal do range:"))
valor_final_range = int(input("Digite o valor final do range:"))

for n in range(valor_inicial_range, valor_final_range):
    print("Valor de n: %d" % n)
