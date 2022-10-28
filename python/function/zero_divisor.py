def division(dividend, divider):
    if type(dividend) != int or type(divider) != int:
        print(f"for this operation dividend and divider must be of type integer")
        return  # para a execução da função
    if divider == 0:
        print(f"divider error cannot be zero!!")
        return  # para a execução da função faz o que o brake faria em outra situação
    return dividend // divider


print(division(8, 2))
