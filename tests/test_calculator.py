import unittest
from src.calculator import sum, subtract, multiplay, divide


class CalculatorTests(unittest.TestCase):

    def test_sumar(self):
        assert sum(2,3) == 5

    def test_resta(self):
        assert subtract

    def test_multiplicacion(self):
        assert multiplay(5, 5) == 25

    def test_division(self):
        result = divide(10, 2)
        expected = 5
        assert result == expected
"""
Comando: python -m unittest discover -s <ruta>

Función: Busca y ejecuta pruebas unitarias en el directorio especificado.

Parámetro -s o --start-directory: Especifica el directorio desde donde unittest debe comenzar a buscar pruebas.

Ejemplo:

bash
python -m unittest discover -s tests

Este comando busca y ejecuta todas las pruebas unitarias en la carpeta tests del proyecto.
"""
