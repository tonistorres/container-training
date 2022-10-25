"""
Você pode usar números de índice {0}para garantir que os
argumentos sejam colocados nos espaços reservados corretos:



"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
