"""
Quebre o loop quando xfor 3 e veja o que acontece com o elsebloco:
"""

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")
