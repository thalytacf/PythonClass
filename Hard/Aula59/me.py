
class Calc:
    def __init__(self, numero1, numero2):
        # variável de classe
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        self.__resultado = self.__n1 + self.__n2
        return self.__resultado

    def subtracao(self):
        self.__resultado = self.__n1 - self.__n2
        return self.__resultado

    def multiplicacao(self):
        self.__resultado = self.__n1 * self.__n2
        return self.__resultado

c =Calc(2,5)
assert c.soma() == 7
assert c.subtracao() == -3
assert c.multiplicacao() == 10
