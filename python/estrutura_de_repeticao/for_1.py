"""
No exemplo que acabamos de ver, a variável n é inicialmente ajustada
para 0 (inicialização com valor padrão).
Uma vez que n é menor do que 10 (condição), o comando print é executado.
Essa condição é adicionada com o comando range.
A variável n é incrementada em 1 (incremento padrão) e é testado se o
valor de n ainda é menor do que 10.
O processo se repete até que o valor de n fique maior ou igual a 10.
"""

for n in range(10):
    print("Nuber: %d" % n)
