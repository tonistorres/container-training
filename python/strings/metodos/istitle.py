"""
Definição e uso
O istitle()método retornará True se todas as palavras em um texto
começarem com uma letra maiúscula E o restante da palavra forem letras
minúsculas, caso contrário, False.

Símbolos e números são ignorados.

Sintaxe
string.istitle()

"""

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)


a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print("Resultado de a: ", a.istitle())
print("Resultado de b: ", b.istitle())
print("Resultado de c: ", c.istitle())
print("Resultado de d: ", d.istitle())
