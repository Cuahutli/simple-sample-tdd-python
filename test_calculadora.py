import unittest
from calculadora import Calculadora

class TestsBasicos(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_una_calculadora_nueva_inicia_en_cero(self):
        self.assertEqual(0,self.calc.valor())

    def test_la_suma_2_mas_3_debe_dar_5(self):
        self.calc.suma(2,3)
        self.assertEqual(5,self.calc.valor())

    def test_la_suma_4_mas_3_debe_dar_7(self):
        self.calc.suma(4,3)
        self.assertEqual(7,self.calc.valor())
