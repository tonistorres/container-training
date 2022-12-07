import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


ALTURAS_FUNCIONARIOS = np.array(
    [[160], [165], [171], [174], [179], [181], [185], [188], [191], [200]]
)


PESO = np.array([[64], [67], [70], [80], [77], [81], [87], [94], [101], [102]])


plt.scatter(ALTURAS_FUNCIONARIOS, PESO)
# plt.show()


regressor = LinearRegression()
regressor.fit(ALTURAS_FUNCIONARIOS, PESO)
print(f"Array do Regressor intercept: {regressor.intercept_}")
print(f"Array do Regressor Coeficiente: {regressor.coef_}")

# fazendo uma previsão paseado nos dados que temos
previsao = regressor.intercept_ + regressor.coef_ * 190
print(
    f"""Baseado em nossas bases de treinamentos\n
    um funcionario de 1m e 90cm ele terá\n
    o peso de; {previsao}"""
)

previsao_sklarne = regressor.predict(np.array([190]).reshape(1, 1))
print(f"Previsão pronta de um funcionario de altura 1.90: {previsao_sklarne}")

previsao_base_inteira = regressor.predict(ALTURAS_FUNCIONARIOS)
print("Previsão de toda minha base :\n", previsao_base_inteira)

resultado_diferenca = PESO - previsao_base_inteira

print("Deferenças relacionadas ao PESO:\n", resultado_diferenca)

resultado_diferenca = abs(PESO - previsao_base_inteira)
print("Deferenças ABSOLUTA relacionadas ao PESO:\n", resultado_diferenca)

resultado_diferenca = abs(PESO - previsao_base_inteira).mean()
print("A Méida desse resultado PESO:\n", resultado_diferenca)

mae = mean_absolute_error(PESO, previsao_base_inteira)
print("Resultado mea:", mae)

mse = mean_squared_error(PESO, previsao_base_inteira)
print("Resultado msq:", mse)

plt.plot(ALTURAS_FUNCIONARIOS, PESO, "o")
plt.plot(ALTURAS_FUNCIONARIOS, previsao_base_inteira, color="red")
plt.title("Regressão Linear Simples")
plt.xlabel("Alturas")
plt.ylabel("Pesos")
plt.show()
