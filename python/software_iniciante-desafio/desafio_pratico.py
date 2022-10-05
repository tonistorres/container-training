def convert():
    value_reais = float(input("Digite o valor em Reais a ser convertido R$:"))
    dollar_count_value = float(input("Digite o valor da contação do Dólar U$:"))
    result = value_reais / dollar_count_value
    print("O valor em Dólar é U$ {}".format(result))


convert()
