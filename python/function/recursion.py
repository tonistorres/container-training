"""

Recursão
Python também aceita recursão de função, o que significa que uma função definida pode chamar a si mesma.

A recursão é um conceito matemático e de programação comum. Isso significa que uma função chama a si mesma.
 Isso tem a vantagem de significar que você pode percorrer os dados para chegar a um resultado.

O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escrever
 uma função que nunca termina, ou uma que usa quantidades excessivas de memória ou poder do
 processador. No entanto, quando escrita corretamente, a recursão pode ser uma abordagem de
 programação muito eficiente e matematicamente elegante.

Neste exemplo, tri_recursion() é uma função que definimos para chamar a si mesma
 ("recurse"). Usamos a variável k como os dados, que decrementam ( -1 ) toda vez que recorremos.
  A recursão termina quando a condição não for maior que 0 (ou seja, quando for 0).

Para um novo desenvolvedor, pode levar algum tempo para descobrir
 exatamente como isso funciona, a melhor maneira de descobrir é testando e modificando.



"""


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
