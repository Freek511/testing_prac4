# our tests here
import math
import unittest
from functions import simpson_integration

class TestSimpsonIntegration(unittest.TestCase):
    def test_simpson_integration_parabola(self):
        f = lambda x: x**2
        a = 0
        b = 1
        n = 10
        result = simpson_integration(f, a, b, n)
        self.assertAlmostEqual(result, 1/3, delta=1e-6)
    
    def test_simpson_integration_exponent(self):
        f = lambda x: math.exp(x)
        a = -10
        b = 10
        n = 100
        result = simpson_integration(f, a, b, n)
        self.assertAlmostEqual(result, 22026.46574940679, delta=1e-6)

if __name__ == '__main__':
    unittest.main()