import unittest
from src.calculator import sum, subtract


class CalculatorTests(unittest.TestCase):

    def test_sumar(self):
        assert sum(2,3) == 5

    def test_resta(self):
        assert subtract

#comando para correr es python -m unittest discover -s