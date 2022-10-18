"""
Você não pode copiar uma lista simplesmente digitando list2 = list1,
porque: list2 será apenas uma referência a list1, e as alterações
feitas em list1 serão feitas automaticamente também em list2.

Existem maneiras de fazer uma cópia, uma delas é usar o método
de lista interno copy().
"""
# Faça uma cópia de uma lista com o método copy():

thislist = ["apple", "banana", "cherry"]
# utilizando o método copy para fazer uma cópida da lista
# thisList para mylist
mylist = thislist.copy()
print(mylist)
