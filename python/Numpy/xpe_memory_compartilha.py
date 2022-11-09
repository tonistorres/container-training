import numpy as np

print(
    f"""-----------------------------------------------
   Observação Importante Sobre Compartilhamento
   de Memória em sub-arrays
-----------------------------------------------
* Sliece compartilha a mesma posição de memória do array original;
* Caso você não queira modificar a construção do seu array original
  aconselhavel usar o método copy dessa forma os elementos de x
  permaneceram intáctos;

"""
)
l = [1, 2, 3]
x = np.array(l)
print(f"x antes:", x)
y = x[:2]  # fazendo um slice do índece 0,1,2
y[0] = -100  # alteração no valor de y altera o valor de x
print("x depois:", x)


lcopy = [2, 5, 9]
x_copy = np.array(lcopy)
print(f"x_copy antes:", x_copy)
y_copy = x_copy[:2].copy()
y_copy[0] = -100
print(f"x_copy depois:{x_copy}")
