"""Модуль тестирования логики функции вычисления квадратного уравнения"""
import unittest
from logic import kvur


class TestKvurFunction(unittest.TestCase):
    """Тест функции kvur при D > 0"""

    def test_discriminant_positive(self):
        """Проверка всех элементов кортежа при D > 0"""
        result = kvur(1, -3, 2)

        self.assertEqual(
            result[0],
            "Квадратное уравнение. D >0. Два корня уравнения"
        )
        self.assertEqual(result[1], 1)

        # Проверяем корни, независимо от порядка
        roots = sorted([result[2], result[3]])
        self.assertAlmostEqual(roots[0], 1.0)
        self.assertAlmostEqual(roots[1], 2.0)
