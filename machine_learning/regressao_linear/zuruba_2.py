import numpy as np
import matplotlib.pyplot as plt

# importando do pacoto sklearn a função de Regresão Linear
from sklearn.linear_model import LinearRegression

# gerando valores com sklearn
from sklearn.datasets import make_regression

# Instanciando a classe de regressão linear
lr = LinearRegression()

# gerando dados para nosso modelo
X, Y = make_regression(n_samples=250, n_features=1, noise=21, random_state=5)
# gerando gráfico do modelo gerado

modelo_linear = lr.fit(X, Y)
# Coeficiente e intercepto
print("Coeficiente:", modelo_linear.coef_)
print("Intercepto:", modelo_linear.intercept_)

plt.scatter(X, Y)
plt.grid(True)
plt.show()
