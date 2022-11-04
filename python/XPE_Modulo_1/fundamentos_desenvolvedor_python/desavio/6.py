# atividade 6 (bem confusa mais acho que deu para resolver)
# relação de dias da semana que cada médico atende
cardiologista = {"terca", "quarta"}
ortopedista = {"terca", "quinta"}
medico_teste = {"segunda", "sexta"}
dermatologista = {"segunda", "quarta", "sexta"}
neurologista = {"terca", "quinta", "sexta"}
psiquiatra = {"segunda ", "quarta", "sexta"}


# Calcula quais os dias possíveis para dois médicos
def disp_dois_especialistas(medico01, medico02):
    str_1 = "Invalido: as agendas combinam apenas 1 dia:"
    str_0 = "Invalido: as agendas são totalmente incompatíveis"
    result = medico01.intersection(medico02)
    if len(result) != 2 and len(result) == 1:
        return f"{str_1} {result}"
    elif len(result) != 2 and len(result) == 0:
        return f"{str_0}"
    else:
        return f"As Agenda dos 2 medicos combinam para: {result}"


result_1 = disp_dois_especialistas(ortopedista, cardiologista)
result_2 = disp_dois_especialistas(ortopedista, neurologista)
result_3 = disp_dois_especialistas(ortopedista, medico_teste)
print(result_1)
print(result_2)
print(result_3)

# Calcula quais os dias possíveis para três Médicos
def disp_tres_especialistas(medico01, medico02, medico03):
    str_1 = "As agendas combinam apenas 1 dia:"
    str_2 = "As agendas combinam apenas 2 dias:"
    str_0 = "As agendas são totalmente incompatíveis"
    result = medico01.intersection(medico02, medico03)
    if len(result) != 3 and len(result) == 2:
        return f"{str_2} {result}"
    elif len(result) != 3 and len(result) == 1:
        return f"{str_1} {result}"
    elif len(result) != 3 and len(result) == 0:
        return f"{str_0} {result}"
    else:
        return f"As Agenda dos 3 medicos combinam para: {result}"


print(disp_tres_especialistas(dermatologista, neurologista, psiquiatra))
