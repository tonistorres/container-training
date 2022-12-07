import numpy as np
import matplotlib.pyplot as plt

# importando do pacoto sklearn a função de Regresão Linear
from sklearn.linear_model import LinearRegression

# gerando valores com sklearn
from sklearn.datasets import make_regression

# Instanciando a classe de regressão linear
lr = LinearRegression()

# Criando os dados que irão popular o modelo
# função numpy.linspace()
# A função linspace() retorna números uniformemente espaçados em um intervalo especificado [start, stop].
# O ponto final do intervalo pode opcionalmente ser excluído.
# https://www.w3resource.com/numpy/array-creation/linspace.php
X = np.linspace(0, 9, 10).reshape(-1, 1)
Y = np.linspace(0, 27, 10).reshape(-1, 1)
print("X:\n", X)
print("Y:\n", Y)

modelo_linear = lr.fit(X, Y)

# Coeficiente e intercepto
print("Coeficiente:", modelo_linear.coef_)
print("Intercepto:", modelo_linear.intercept_)

# gerando o gráfico do modelo gerado

plt.plot(X, Y)
plt.grid(True)
plt.show()
