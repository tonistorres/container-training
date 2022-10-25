"""

O método format() recebe um número ilimitado de argumentos
e são colocados nos respectivos espaços reservados:


"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print("I want {} pieces of item {} for {} dollars.".format(quantity, itemno, price))
