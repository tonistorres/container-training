"""
Definição e uso
O isalnum()método retornará True se todos os caracteres forem alfanuméricos,
 ou seja, letra do alfabeto (az) e números (0-9).

Exemplo de caracteres que não são alfanuméricos: (espaço)!#%&? etc.

"""

txt = "Company12"

x = txt.isalnum()

print(x)


t = "Company 12"

y = t.isalnum()

print(y)
