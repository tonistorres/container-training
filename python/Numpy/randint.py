import numpy as np

# gerar um numero  aleatório entre 0 e 8

print(np.random.randint(9))


# gerar vários números aleatórios
print(np.random.randint(10, 21, size=20))


# gerar vários números aleatórios bidimenssional
print(np.random.randint(1, 31, size=(4, 5)))
