# Exemplo
# Calcule o MODO e substitua quaisquer valores vazios por ele:

import pandas as pd
import module_head as r

df = pd.read_csv("data.csv")

x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)
r.head(",", "Preenchendo valor mais frequente")
print(df)


# Moda = o valor que aparece com mais frequência.
