# Retorne um novo Data Frame sem células vazias:

import pandas as pd

df = pd.read_csv("data.csv")

df.fillna("nulo", inplace=True)

print(df.to_string())
