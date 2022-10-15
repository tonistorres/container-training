# Os itens da lista podem ser de qualquer tipo de dados:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
# Uma lista com strings, números inteiros e valores booleanos:
list4 = ["abc", 34, True, 40, "male"]


print("list1:{}".format(list1))
print("list2:{}".format(list2))
print("list3:{}".format(list3))
print("list4:{}".format(list4))

# Também é possível usar o construtor list() ao criar uma nova lista.
thislist = list(("apple", "banana", "cherry"))
print("Criando uma lista por meio de um construtor:{}".format(thislist))

print("Tamnho list1 {}".format(len(list1)))
print("Tamnho list2 {}".format(len(list2)))
print("Tamnho list3 {}".format(len(list3)))
print("Acessando indice 1 list1:{}".format(list1[1]))
print("Acessando indice 2 list1:{}".format(list2[2]))
print("Acessando indice 0 list1:{}".format(list3[0]))
