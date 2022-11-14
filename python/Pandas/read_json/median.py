# Calcule a MEDIAN e substitua quaisquer valores vazios por ela:

import pandas as pd
import module_head as rhead

df = pd.read_csv("data.csv")

x = df["Calories"].median()

df["Calories"].fillna(x, inplace=True)
rhead.head(",", "Preenchendo Median")
print(df)
