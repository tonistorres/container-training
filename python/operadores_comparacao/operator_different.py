# Operador igual :!=
# Desenvolva uma função  faça uso desse operador.
# https://docs.python.org/pt-br/3/library/stdtypes.html#boolean-operations-and-or-not


def enter_str(str_one, str_two):
    if len(str_one) != len(str_two):
        print("O tamanho da string one é diferente da string two")
    else:
        print("O tamanho da string two é diferente da string one")


enter_str("tonis", "alberto")
