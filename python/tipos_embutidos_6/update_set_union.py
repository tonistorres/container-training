# O update()método insere os itens em set2 em set1:
# Nota: Ambos union()e update() excluirão quaisquer itens duplicados.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
