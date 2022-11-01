"""
O primeiro parâmetro, o self, representa a instância do objeto,
ou seja, tem acesso ao objeto na memória. Com o método init,
inicializamos os atributos do objeto apenas atribuindo um valor
a cada nova chave.
Exemplo: self.ligado = False.

"""


class Liquidificador:
    def __init__(self, cor, potencia, voltagem, preco):
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.preco = preco
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__amperagem_atual_no_motor = 0

    # https://www.youtube.com/watch?v=dQqR4EmmXSk
    def __str__(self):
        return f"Objeto Liquidificador:\n Cor:{self.__cor}\n Ligado:{self.__ligado}\n Potência:{self.__potencia}\n Voltagem:{self.__voltagem}\n Preço:{self.preco}\n Amperagem do Motor:{self.__amperagem_atual_no_motor}\n Velocidade:{self.__velocidade}"

    # criando um método para aumentar a velocidade
    def velocidade(self, velocidade):

        if (self.__ligado == True) and (
            velocidade > 0 and velocidade <= self.__velocidade_maxima
        ):
            self.__velocidade = velocidade
            self.__amperagem_atual_no_motor = (
                (self.__potencia / self.__voltagem) / self.__velocidade_maxima
            ) * velocidade
        else:
            raise ValueError(f"Liquidificador desligado ou Velocidade incompatível")

    # método para ligar e desligar o Liquidificador
    def liga_desliga(self, valor_booleano):

        if valor_booleano == False:
            self.__velocidade = 0
            self.__ligado = False
            self.__potencia = 0
            self.__voltagem = 0
            self.__amperagem_atual_no_motor = 0

        elif valor_booleano == True:
            # self.__velocidade = 0
            self.__ligado = True
            self.__amperagem_atual_no_motor = 0

        else:
            print("Só aceitamos valores Boleanos True ou False")

    # Getter
    @property
    def cor(self):
        return self.__cor

    # Setter
    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


liquidificador = Liquidificador("Verde", 200, 220, 350)
liquidificador.cor = "orange"
liquidificador.liga_desliga(True)
liquidificador.velocidade(2)

liquidificador_2 = Liquidificador("Verde", 200, 220, 350)
liquidificador_2.liga_desliga(True)
liquidificador_2.velocidade(3)


print(f"{liquidificador}")
print(f"{liquidificador_2}")
