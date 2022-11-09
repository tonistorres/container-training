import pandas as pd
import numpy as np

data = {
    "animal": [
        "cat",
        "cat",
        "snake",
        "dog",
        "dog",
        "cat",
        "snake",
        "cat",
        "dog",
        "dog",
    ],
    "age": [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
    "visits": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "priority": ["yes", "yes", "no", "yes", "no", "no", "no", "yes", "no", "no"],
}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

#
x = pd.DataFrame(data=data, index=labels)
df = pd.DataFrame(data=data, index=labels)
linha = "***********************************"
print(
    f"\n{linha}\n Report Question 8 \n{linha}\n{x}\n{linha}\n dimension -->> {x.shape}\n{linha}\n"
)
print(
    f"\n{linha}\n Report Question 9 \n{linha}\n{df}\n{linha}\n dimension -->> {df.shape}\n{linha}\n"
)
