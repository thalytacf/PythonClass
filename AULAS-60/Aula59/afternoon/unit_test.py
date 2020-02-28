import unittest
from metodos import Calculus


class TestCalculus(unittest.TestCase):
    objeto = Calculus(10,5)

    def test_soma(self):
        self.assertEqual(self.objeto.a, 10, '20 não é igual a objeto.a')
        self.assertEqual(self.objeto.b, 5, 'Teste2 msg')
        self.assertIsInstance(self.objeto, Calculus)



if __name__ == '__main__':
    unittest.main()