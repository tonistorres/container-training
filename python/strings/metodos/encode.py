"""
Método Python String codificar()

Exemplo
UTF-8 codifica a string:
O encode()método codifica a string, usando a codificação especificada.
Se nenhuma codificação for especificada, UTF-8 será usado.
"""

txt = "My name is Ståle"

x = txt.encode()

print(x)


txt_2 = "My name is Ståle"


# Esses exemplos usam codificação ASCII e um caractere que não pode ser codificado,
# mostrando o resultado com diferentes erros:
print(txt_2.encode(encoding="ascii", errors="backslashreplace"))
print(txt_2.encode(encoding="ascii", errors="ignore"))
print(txt_2.encode(encoding="ascii", errors="namereplace"))
print(txt_2.encode(encoding="ascii", errors="replace"))
print(txt_2.encode(encoding="ascii", errors="xmlcharrefreplace"))
