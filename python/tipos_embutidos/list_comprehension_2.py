"""
A compreensão de lista oferece uma sintaxe mais curta quando
você deseja criar uma nova lista com base nos valores de uma
lista existente.
Exemplo:
Com base em uma lista de frutas, você deseja uma nova lista,
contendo apenas as frutas com a letra "a" no nome.
Sem compreensão de lista, você terá que escrever uma instrução
for com um teste condicional dentro:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
# percorrer a lista de frutas elementos por elementos
for x in fruits:
    # se tiver a letra a no elemento percorrido
    if "a" in x:
        # adicione esse elemento na nova lista por meio do método
        # append
        newlist.append(x)
# imprima a nova lista
print("Result used for: {}".format(newlist))


fruits_compreension = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist_compreension = [x for x in fruits_compreension if "a" in x]

print("Result List Compreension:{}".format(newlist_compreension))
