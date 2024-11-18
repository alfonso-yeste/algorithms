"""
librería para hacer test
"""
import unittest

from cadena_invertida import invertir_cadena

class TestCadenaInvertida(unittest.TestCase):

    def test_invertir_palabra(self):
        self.assertEqual(invertir_cadena('Hola'), 'aloH')
        self.assertEqual(invertir_cadena('h'), 'h')
        self.assertEqual(invertir_cadena(''), '')
        self.assertEqual(invertir_cadena('hol   a'), 'a   loh')

    def test_invertir_frase(self):
        self.assertEqual(invertir_cadena('Hola mundo'), 'odnum aloH')

    def test_invertir_numeros(self):
        self.assertEqual(invertir_cadena('12345'), '54321')



if __name__ == '__main__':
    unittest.main()




