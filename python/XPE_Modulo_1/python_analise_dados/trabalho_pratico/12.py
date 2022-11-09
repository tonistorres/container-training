import pandas as pd
import numpy as np
import module_head as hreport
import module_fotter as freport

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

df = pd.DataFrame(data=data, index=labels)
linha = "***********************************"

print(
    f"\n{linha}\n Report Question 8,9 \n{linha}\n{df}\n{linha}\n dimension -->> {df.shape}\n{linha}\n"
)
hreport.head("*", "Report Question 11")
# contando de cima para baixo de acordo
# com que apareceu para mim tendo em vista
# que as respostas da xp se embralham automagicamente
print("a)Correct - \n", df["visits"])
print("b)Correct - \n", df.iloc[:, -2])
print("c)Correct - \n", df.loc[:, "visits"])
print("d)Wrong  - \n", df.iloc[:, 3])
freport.fotter("*", "End Report")
