# ativida 4
# Excelente vídeo para entender essa dinâmica: https://www.youtube.com/watch?v=xmMXULd0dxc
# Se precisarem de mais informação: https://www.w3schools.com/python/python_lambda.asp
# importando biblioteca nativa do python
import math

# area do circulo recebe radius como parâmetro lambda radius
# e retorna o calculo da área para area_cicle
area_circle = lambda radius: math.pi * (radius**2)
# criando uma variável de nome result que recebe (guarda na memória)
# o resultado (retorno) do cálculo de uma função anônima(lambda)
# com o resultado da área
# Observação é importante ressaltar que quando eu passo como argumento
# o valor 8(oito) para a função area_cicle(8) esse 8 é passado como valor
# para radius que permite efetuar os cáculos da função
result = area_circle(8)
# nesse ponto estou usando mascara para poder imprimir o resultado
# do tipo real (float) com duas casas decimais apenas isso tudo para
# porque o valor de PI é meio exagerado se é que me entende.
print("Area is %.2f :" % result)

# bem não irei explicar essa por que é a mesma dinâmica da função
# acima já elucidada com uma pequena diferença no que diz respeito
# que é passado dois parâmetros
area_circle_two = lambda radius, PI: PI * (radius**2)
result_two = area_circle_two(8, 3.14)
print("The result two is %.2f:" % result_two)
