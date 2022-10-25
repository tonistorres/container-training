"""
String Python termina com () Método

Exemplo
Verifique se a string termina com um sinal de pontuação (.):


"""

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

# Verifique se as posições 5 a 11 terminam com a frase "meu mundo".:

txt_2 = "Hello, welcome to my world."

y = txt_2.endswith("my world.", 5, 11)

print(y)
