# Exercício 4: Suponha que o preço de capa de um livro
# seja R$ 24,20, mas as livrarias recebem um desconto de 40%.
# O transporte custa 3,00 para o primeiro exemplar e 75 centavos
# para cada exemplar adicional. Qual é o custo total de atacado
# para 60 cópias? Escreva uma expressão que receba o custo total
#  e a imprima.

# Preço do livro 24,20
# Livraria recebe desconto 40%(9,68), logo,14,52.
# Transporte primeiro exemplar 3,00
# cada Exemplar adicional 0,75
# valor_bruto = 14,52*60 = 871,2

# transporte_1 =(numero_exemplar -1) * 0,75
# transport_1 = 44,25
# transporte_total = 3 + transporte_1
# transporte_total = 3 + 44,25
# transporte_total = 47,25
# custo_total_atacado_n_copias = valor_bruto -transporte_total

num_copias = int(input("Digite o numério de copias a serem transopotadas:"))
preco_liq_livro = float(input("Digite o preço Líquido de uma copia: "))


def custo_total_atacado(num_copias, preco_liq_livro):
    livro_com_desconto = preco_liq_livro - (preco_liq_livro * 40 / 100)
    valor_sem_transporte = livro_com_desconto * num_copias
    transporte = 3 + (num_copias - 1) * 0.75
    custo_total = valor_sem_transporte - transporte
    print("Livro com Desconto: %.2f" % livro_com_desconto)
    print("Valor sem Transporte: %.2f" % valor_sem_transporte)
    print("Transporte: %.2f" % transporte)
    print("Custo Total: %.2f" % custo_total)


custo_total_atacado(num_copias, preco_liq_livro)
