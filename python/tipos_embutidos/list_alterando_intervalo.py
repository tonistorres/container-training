"""

Alterar um intervalo de valores de itens
Para alterar o valor dos itens dentro de um intervalo específico,
 defina uma lista com os novos valores e consulte o intervalo de
  números de índice onde deseja inserir os novos valores
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
