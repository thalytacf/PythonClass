from metodos import Calculus

class TestMetodos():

    def __init__(self):
        self.objeto = Calculus(10,5)

    def test_soma(self):
        try:
            assert self.objeto.a == 10
            assert self.objeto.b == 5
            assert self.objeto.soma() == 15
            return '\033[32m°passou no teste da soma()\033[m'

        except AssertionError:
            return '\033[31m°Não passou no teste da soma()\033[m'

    def test_subtracao(self):
        try:
            assert self.objeto.a == 10
            assert self.objeto.b == 5
            assert self.objeto.subtracao() == 5
            return '\033[32m°passou no teste da subtracao()\033[m'

        except AssertionError:
            return '\033[31m°Não passou no teste da subtracao()\033[m'

    def test_produto(self):
        try:
            assert self.objeto.a == 10
            assert self.objeto.b == 5
            assert self.objeto.produto() == 50
            return '\033[32m°passou no teste do produto()\033[m'

        except AssertionError:
            return '\033[31m°Não passou no teste do produto()\033[m'

    def test_divisao(self):
        try:
            assert self.objeto.a == 10
            assert self.objeto.b == 5
            assert self.objeto.divisao() == 2
            return '\033[32m°passou no teste da divisao()\033[m'

        except AssertionError:
            return '\033[31m°Não passou no teste da divisao()\033[m'


teste = TestMetodos()
print('\nResultado dos Testes com Asserts\n')
print(teste.test_soma())
print(teste.test_subtracao())
print(teste.test_produto())
print(teste.test_divisao())