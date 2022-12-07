import numpy as np
import matplotlib.pyplot as plt


# ALTURAS_FUNCIONARIOS = np.array(
#     [[160], [165], [171], [174], [179], [181], [185], [188], [191], [200]]
# )


# PESO = np.array([[64], [67], [70], [80], [77], [81], [87], [94], [101], [102]])

X = np.arange(1, 6)

# colocamos um estilo no gráfico
plt.style.use("ggplot")
# startando metodo iterativo do gráfico
plt.ion()

for i in range(30):
    # Gerando novo dados para um novo grafico após 3s
    DADOS = np.random.randint(20, 30, 5)
    print(f"X:{X} Dados:{DADOS}")
    # limpa a área do grafico conteudo
    plt.cla()
    # limpando toda janela do grafico
    plt.clf()
    # capturando os dados e alimentando o gráfico
    plt.bar(X, DADOS)
    plt.pause(1)


# desligando o módulo iterativo
plt.ioff()
# mantendo a ultima exibiçao do grafico na tela
plt.show()
