import pandas as pd
import numpy as np
import module_head as hreport
import module_fotter as freport

y_true = np.array([1.0, 2.0, 1.0])
y_pred = np.array([1.1, 1.98, 1.05])

result = np.sqrt(((y_true - y_pred) ** 2).mean())

hreport.head("*", "Report Question 14")
print(result)
freport.fotter("*", "End Report")
