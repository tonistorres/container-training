"""
Adicionar conjuntos
Para adicionar itens de outro conjunto ao conjunto atual,
use o update() método.
"""

# Adicione elementos de tropicalinto thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
