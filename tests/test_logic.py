"""Модуль тестирования логики функции вычисления квадратного уравнения"""
import unittest
from logic import kvur  


class TestKvurFunction(unittest.TestCase):

    def test_discriminant_positive(self):
        # Пример уравнения: x^2 - 3x + 2 = 0, D = 1, корни 2 и 1
        result = kvur(1, -3, 2)
        self.assertEqual(result[0], "Квадратное уравнение. D >0. Два корня уравнения")
        self.assertEqual(result[1], 1)  # D
        roots = sorted([result[2], result[3]])  # Сортировка, если порядок корней поменяется
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 2.0)

if __name__ == '__main__':
    unittest.main()
