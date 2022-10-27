"""
Junte dois conjuntos
Existem várias maneiras de unir dois ou mais conjuntos em Python.

Você pode usar o union()método que retorna um novo conjunto contendo
 todos os itens de ambos os conjuntos ou o update()método que insere
 todos os itens de um conjunto em outro:


"""
# Nota: Ambos union()e update() excluirão quaisquer itens duplicados.
# O union()método retorna um novo conjunto com todos os itens de ambos os conjuntos:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
