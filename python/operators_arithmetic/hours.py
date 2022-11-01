# Exercício 2: Declare e inicialize uma variável:
# hours = 6. Quantos minutos têm em 6 horas? E
# quantos segundos? Declare e inicialize variáveis
# minutes e seconds que recebem os respectivos resultados
# das contas. Depois, imprima cada uma delas.


def calcule_minutos_segundos(horas):
    minutes = horas * 60
    seconds = horas * (60 * 60)
    print("Horas %d" % minutes, "minutos")
    print("Segundos %d" % seconds, "segundos")


calcule_minutos_segundos(1)
