import unittest
from functions import *

class TestEquationSolver(unittest.TestCase):
    def test_linear_solver1(self):
        power = 1
        coeffs = [1, 2]
        result = equation_solver(coeffs, power)
        expected_result = -0.5
        self.assertEqual(result, expected_result)

    def test_linear_solver2(self):
        power = 1
        coeffs = [1, 0]
        result = equation_solver(coeffs, power)
        expected_result = 'No answers'
        self.assertEqual(result, expected_result)

    def test_linear_solver3(self):
        power = 1
        coeffs = [0, 0]
        result = equation_solver(coeffs, power)
        expected_result = 'Any number'
        self.assertEqual(result, expected_result)

    def test_square_solver1(self):
        power = 2
        coeffs = [2, 3, 1]
        result = equation_solver(coeffs, power)
        expected_result = (-1.0, -2.0)
        self.assertEqual(result, expected_result)

    def test_square_solver2(self):
        power = 2
        coeffs = [1, 2, 3]
        result = equation_solver(coeffs, power)
        expected_result = 'No answers'
        self.assertEqual(result, expected_result)

    def test_square_solver3(self):
        power = 2
        coeffs = [1, 2, 1]
        result = equation_solver(coeffs, power)
        expected_result = -1.0
        self.assertEqual(result, expected_result)

    def test_qubic_solver(self):
        power = 3
        coeffs = [1, -2, -1, 3]
        a = -1.0
        b = -0.5
        eps = 0.01
        result = equation_solver(coeffs, power, a, b, eps)
        expected_result = -0.87
        self.assertAlmostEqual(result, expected_result, places=2)



if __name__ == '__main__':
    unittest.main()
