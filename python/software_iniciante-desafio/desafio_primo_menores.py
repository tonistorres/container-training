def prime_number(number):
    count_divisible = 0
    for c in range(1, number + 1):
        if number % c == 0:
            count_divisible += 1

    if count_divisible == 2:
        print("\033[m Esse numero é primo  {}".format(number))
        return number


def range_prime(number_min, number_max):
    arr_number_prime = []
    summation = 0
    for c in range(number_min, number_max):
        return_number_prime = prime_number(c)
        if return_number_prime != None:
            arr_number_prime.append(return_number_prime)
    print(f"O resultado é: {arr_number_prime}")
    for number in arr_number_prime:
        summation += number
    print(f"primos menores que numero passado por argumento e: {summation}")


range_prime(4, 15)
