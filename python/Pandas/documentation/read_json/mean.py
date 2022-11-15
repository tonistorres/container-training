# Substituir usando média, mediana ou modo
# Uma maneira comum de substituir células vazias é calcular o valor médio, mediano ou moda da coluna.

# O Pandas usa os métodos mean() median()e mode()para calcular os respectivos valores para uma coluna especificada:

# Exemplo
# Calcule a MÉDIA e substitua quaisquer valores vazios por ela:

import pandas as pd
import module_head as rhead

df = pd.read_csv("data.csv")

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace=True)
rhead.head("-", "Preenchendo com a média")
print(df)
