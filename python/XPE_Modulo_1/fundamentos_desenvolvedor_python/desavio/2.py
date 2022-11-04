# atividade 2

# sintaxe dict comprehension sem condicional
# {chave:valor for item in range()}

# Os dicionários são usados ​​para
# armazenar valores de dados em pares chave:valor.

# Um dicionário é uma coleção ordenada*, mutável
# e que não permite duplicatas.
# OBSERVAÇÃO: Assim como a estrutura set/conjunto
# os dicionários não aceitam repetição na sua estrutura

# lista de strings
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
# list comprehension - nessa linha de código
# poderíamos interpretar o código como sendo
# crie um novo dicionário percorrendo toda lista
# de nomes item a item e montando a estrutura do
# dicionario com os nomes contido na lista em sua
# chave e o tamanho ou a quantidade de caracter
# no seu valor
dict_new = {nome: len(nome) for nome in nomes}
#  imprima o dicionário
print(dict_new)
# para desencargo de conciência me dica o tipo dessa
# estrutura por meio da função type nativa do python
print(type(dict_new))
