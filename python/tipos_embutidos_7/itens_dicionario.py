"""
Itens do dicionário
Os itens do dicionário são ordenados, alteráveis ​​e não permitem duplicatas.

Os itens do dicionário são apresentados em pares chave:valor
 e podem ser referenciados usando o nome da chave.

Ordenado ou Não Ordenado?
A partir da versão 3.7 do Python, os dicionários são ordenados .
 No Python 3.6 e anteriores, os dicionários não são ordenados .

Quando dizemos que os dicionários estão ordenados, significa
que os itens têm uma ordem definida, e essa ordem não será alterada.

Não ordenado significa que os itens não têm uma ordem definida,
 você não pode fazer referência a um item usando um índice.

Mutável
Os dicionários são mutáveis, o que significa que podemos alterar,
adicionar ou remover itens após a criação do dicionário.

Duplicatas não permitidas
Os dicionários não podem ter dois itens com a mesma chave:


"""

# Exemplo
# Imprima o valor "marca" do dicionário:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])
