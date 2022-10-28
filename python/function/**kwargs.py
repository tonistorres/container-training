"""
Argumentos arbitrários de palavras-chave, **kwargs
Se você não souber quantos argumentos de palavra-chave serão
passados ​​para sua função, adicione dois asteriscos: **antes do nome do parâmetro na definição da função.

Desta forma a função receberá um dicionário de argumentos,
podendo acessar os itens de acordo:

"""
# Se o número de argumentos de palavra-chave for desconhecido, adicione um duplo **antes do nome do parâmetro:


def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")
