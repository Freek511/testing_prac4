import unittest
from functions import multiply_matrices


class TestClass(unittest.TestCase):

    def test_multiply_correct_matrices(self):
        m1 = [[1, 2],
              [3, 4],
              [5, 6]]

        m2 = [[1, 2, 3],
              [4, 5, 6]]

        answer = [[9, 12, 15],
                  [19, 26, 33],
                  [29, 40, 51]]

        self.assertEqual(answer, multiply_matrices(m1, m2))

    def test_multiply_matrices_with_different_dimension(self):
        m1 = [[1, 2],
              [3, 4],
              [5, 6]]
        m2 = [[1, 2],
              [3, 4],
              [5, 6]]

        with self.assertRaises(AssertionError):
            multiply_matrices(m1, m2)

    def test_multiply_matrices_invalid_arguments(self):
        m1 = 123
        m2 = dict()
        with self.assertRaises(AssertionError):
            multiply_matrices(m1, m2)


if __name__ == "__main__":
    unittest.main()
