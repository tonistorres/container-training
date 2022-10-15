"""
Você pode especificar um intervalo de índices especificando
onde começar e onde terminar o intervalo.

Ao especificar um intervalo, o valor de retorno será uma nova
lista com os itens especificados.

Ao deixar de fora o valor inicial, o intervalo começará no
primeiro item.
Ao deixar de fora o valor final, o intervalo irá para
o final da lista.

Especifique índices negativos se desejar iniciar a
pesquisa a partir do final da lista.
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[:4])
# print(thislist[2:])
print(thislist[-4:-1])
