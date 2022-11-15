import module_head as r
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("temperature.csv")
r.head(",", "Print CSV Base")
print(df.to_string())
r.head(",", "Extraindo x , y")
x, y = df[["temperatura"]].values, df[["classification"]].values
print("x:\n", x)
print("y:\n", y)
# print(df.to_string())

le = LabelEncoder()
y = le.fit_transform(y.ravel())
print("y_new:\n", y)
