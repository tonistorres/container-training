"""
https://www.youtube.com/watch?v=2gQd0yTE42A
https://www.w3schools.com/python/python_tuples_unpack.asp

Mas, em Python, também podemos extrair os valores
de volta para as variáveis. Isso é chamado de "descompactar"
"""

tuple = ("Tonis", "Alberto", "Ferreira", 42)
# Desempacotando em variáveis
nome, sobre_nome, ultimo_nome, idade = tuple
print(
    f"Nome:{nome}\n Sobre Nome:{sobre_nome}\n Último Nome:{ultimo_nome}\n Idade:{idade}"
)

tuple_composta = (("Tonis", "Torres"), 42)
(nome_composta, sobre_nome_composta), idade_composta = tuple_composta
print(
    f"Nome:{nome_composta}\n Sobre Nome:{sobre_nome_composta}\nIdade:{idade_composta}"
)
