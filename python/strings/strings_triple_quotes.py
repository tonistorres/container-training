# As strings literais podem abranger várias linhas.
#  Uma maneira é usar as aspas triplas: """...""" ou '''...'''.
# O fim das linhas é incluído automaticamente na string, mas é
# possível evitar isso adicionando uma \ no final. O seguinte exemplo:
print(
    """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
)
