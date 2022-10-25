"""
Com a instrução continue podemos parar a iteração
 atual do loop e continuar com a próxima

"""

fruits = ["apple", "banana", "lemon", "cherry"]
for x in fruits:
    if x == "banana" or x == "lemon":
        continue
    print(x)
