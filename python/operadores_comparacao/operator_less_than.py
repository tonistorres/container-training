# Operador Menor que: <
# Desenvolva uma função que faça uso desse operador.
# https://docs.python.org/pt-br/3/library/stdtypes.html#boolean-operations-and-or-not


def enter_str(str_one, str_two):
    if len(str_one) < len(str_two):
        print("a string one menor que string two")
    else:
        print("a string two menor que string one")


enter_str("tonis", "alberto")
