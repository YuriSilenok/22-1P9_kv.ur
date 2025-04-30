"""Модуь тестирования логики функции вычисления квадратного уравнения"""
import unittest
from logic import kvur  


class TestKvurFunction(unittest.TestCase):

    def test_discriminant_positive(self):
       
        result = kvur(1, -3, 2)
        self.assertEqual(result[0], "Квадратное уравнение. D >0. Два корня уравнения")
        self.assertEqual(result[1], 1)  # D
        roots = sorted([result[2], result[3]])  # Сортировка, если порядок корней поменяется
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 2.0)

    def test_discriminant_negative(self):
       
        result = kvur(1, 2, 5)
        self.assertEqual(result, ("Ошибка",))

    def test_zero_coefficient_a(self):
        
        with self.assertRaises(ZeroDivisionError):
            kvur(0, 2, 1)

if __name__ == '__main__':
    unittest.main()
