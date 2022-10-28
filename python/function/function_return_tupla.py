from math import remainder


def division_quotient_remainder(dividend, divider):
    if divider == 0:
        print("this operation is mathematically impossible.")
        return  # para imediatamente a execução da função
    quotient = dividend // divider
    remainder = dividend % divider
    return (quotient, remainder)


print(f"Resultado da função: {division_quotient_remainder(8, 4)}")
