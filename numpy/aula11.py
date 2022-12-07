# https://www.youtube.com/watch?v=SNzRfU84dEo&list=PL3Fmwz_E1hXRWxIkP843DiDf0ZeqgftTy&index=14
# Criando Array a partir de listas

import numpy as np
import convert_real
import matplotlib.pyplot as plt

qutde = [2, 5, 10, 20, 35]
custo = [100, 150, 1110, 105, 108]
qtde_prod_vendido = [1, 3, 4, 5, 15]

qutde_prod_estoque = np.array(qutde)
precompra = np.array(custo)
qtde_prod_vendido_avista = np.array(qtde_prod_vendido)


print(f"\nQtde produtos em Estoque:\n{qutde_prod_estoque}")
print(f"\nP_compra cada produto  R$:\n{precompra}")
print(f"\nQtde_Produto_vendido:\n{qtde_prod_vendido_avista}")
print(f"\nRestante em Estoque:\n{qutde_prod_estoque-qtde_prod_vendido_avista}")
print(
    f"\nPreço_Restante R$:\n{(qutde_prod_estoque-qtde_prod_vendido_avista)*precompra}"
)

# processando a multiplicação entro dois arrays
# aqui teremos consolidado da multiplicação
# de quantidade e custo para chegarmos ao
# valor total de produtos no estoque
valor_real_estoque = np.sum((qutde_prod_estoque - qtde_prod_vendido_avista) * precompra)
# nesse ponto estou usando um módulo externo para converter
# o valor inteiro em real
print(f"Valor Real do Estoque R$:{convert_real.real_br_money_mask(valor_real_estoque)}")

# colocamos um estilo no gráfico
plt.style.use("ggplot")
# acrescentar grid ao gráfico
plt.grid(True)
# limpa a área do grafico conteudo
plt.cla()
# limpando toda janela do grafico
plt.clf()
# etiqueta eixo x
plt.xlabel("Quantidade [Estoque Inicial]")
# etiqueta eixo y
plt.ylabel("Quatidade [Produtos Mais Vendidos]")
# capturando os dados e alimentando o gráfico
plt.bar(qutde_prod_estoque, qtde_prod_vendido_avista)
# mantendo a ultima exibiçao do grafico na tela
plt.show()
