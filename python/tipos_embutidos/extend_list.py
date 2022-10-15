"""
Para anexar elementos de outra lista à lista atual,
use o método extend()
unica uma lista dentro da outra funciona por debaixo dos
panos como um spread
"""


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
