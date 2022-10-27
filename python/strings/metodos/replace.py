"""
Definição e uso
O replace()método substitui uma frase especificada por outra frase especificada.

Nota: Todas as ocorrências da frase especificada serão substituídas,
 se nada mais for especificado.

"""

txt = "I like bananas"

x = txt.replace("bananas", "apples")

# print(x)


# Substitua as duas primeiras ocorrências da palavra "um":

txt2 = "one one was a race horse, two two was one too."

x2 = txt2.replace("one", "three", 2)

print(x2)
