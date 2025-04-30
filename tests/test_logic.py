"""тестирование квадратного уравнения"""
import unittest
from logic import kvur


class TestKvurFunction(unittest.TestCase):
    """Тест функции kvur при D > 0"""

    def test_discriminant_positive(self):
        """Проверка всех элементов кортежа при D > 0"""
        result = kvur(1, -3, 2)

        # Проверка текста
        self.assertEqual(
            result[0],
            "Квадратное уравнение. D >0. Два корня уравнения"
        )

        # Проверка дискриминанта
        self.assertEqual(result[1], 1)

        roots = sorted([result[2], result[3]])
        expected_roots = [1.0, 2.0]
        for actual, expected in zip(roots, expected_roots):
            self.assertAlmostEqual(actual, expected)
