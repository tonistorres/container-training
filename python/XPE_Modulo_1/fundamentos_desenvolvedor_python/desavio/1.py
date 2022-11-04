# Tipo de dados lista
nomes = [
    "Maria",
    "Julieta",
    "Fernando",
    "Cristiano",
    "Julieta",
    "Maria",
    "Fernando",
    "Cláudio",
]
# Temos uma estrutura set:
#  - não aceita repetição de valores
#  - desordenado
qtd_letras = {}

# calcula o tamanho de cada nome (em número de letras) e armazena o valor na estrutura
for nome in nomes:
    # nesse pornto estamos adicionando chaves e valores numa estrutura set
    # e convertando automagicamente em um dicionário
    qtd_letras[nome] = len(nome)
# nesse ponto é um dicionario
# print(qtd_letras)

# print(type(nomes))
# print(type(qtd_letras))

# resposta 1 - lista (list) e dicionário (dict)
# resposta 2 - somente tuplas pode ser chave de um dicionário lista não pode
# print(len({1, 3, 1, 4, 3, 2, 2, 0, 4}))
# print([n / 2 for n in range(0, 10) if n > 3])
print(len(nomes))
print(len(qtd_letras))
