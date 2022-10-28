"""
Para percorrer um conjunto de código um determinado número de vezes,
podemos usar a função range() ,
A função range() retorna uma sequência de números, começando em 0 por padrão
e incrementa em 1 (por padrão)
e termina em um número especificado.

"""
for x in range(6):
    print(x)


"""
A função range() padroniza para incrementar a sequência em 1,
porém é possível especificar o valor do incremento adicionando
 um terceiro parâmetro: range(2, 30, 3 ) :
"""

for y in range(2, 30, 3):
    print(y, end="")
