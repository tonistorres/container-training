# Retorne um novo Data Frame sem células vazias:

import pandas as pd

df = pd.read_csv("data.csv")


print(df)
new_df = df.dropna()

print(new_df.to_string())

