# https://www.youtube.com/watch?v=Wt0kQxYyviA

"""
Junte todos os itens de uma tupla em uma string, usando um caractere de
hash como separador:


"""


# o método join() transforma uma lista em strings

list = ["a", "n", "a", 1]


def convert_with_join():
    try:
        convert_str_join = "".join(list)
        print("Lista convertida em string: ", convert_str_join)
    except TypeError:
        print("Join Espera que todos os itens da lista seja string")


convert_with_join()
