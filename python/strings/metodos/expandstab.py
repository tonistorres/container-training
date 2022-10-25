"""
Método Python String expandtabs()

Exemplo
Defina o tamanho da guia para 2 espaços em branco:
"""
txt = "H\te\tl\tl\to"

x = txt.expandtabs(2)

print(x)


t = "H\te\tl\tl\to"

print(t)
print(t.expandtabs())
print(t.expandtabs(2))
print(t.expandtabs(4))
print(t.expandtabs(10))
