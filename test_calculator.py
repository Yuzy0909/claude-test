"""
test_calculator.py - calculator.py のユニットテスト

実行方法:
    python -m pytest test_calculator.py -v
    # または
    python -m unittest test_calculator.py
"""

import unittest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    floor_divide,
    modulo,
    power,
    calculate,
    SUPPORTED_OPERATORS,
)


class TestAdd(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(add(3, 4), 7)

    def test_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3)

    def test_negative(self):
        self.assertEqual(add(-5, 3), -2)

    def test_type_error_string(self):
        with self.assertRaises(TypeError):
            add("1", 2)

    def test_type_error_none(self):
        with self.assertRaises(TypeError):
            add(None, 2)


class TestSubtract(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(subtract(10, 3), 7)

    def test_negative_result(self):
        self.assertEqual(subtract(3, 10), -7)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            subtract("a", 1)


class TestMultiply(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(multiply(4, 7), 28)

    def test_zero(self):
        self.assertEqual(multiply(0, 999), 0)

    def test_float(self):
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            multiply([1], 2)


class TestDivide(unittest.TestCase):
    def test_basic(self):
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_returns_float(self):
        result = divide(20, 4)
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, 5.0)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            divide("10", 2)


class TestFloorDivide(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(floor_divide(20, 3), 6)

    def test_returns_int(self):
        self.assertIsInstance(floor_divide(7, 2), int)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            floor_divide(5, 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            floor_divide(10, "2")


class TestModulo(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(modulo(20, 3), 2)

    def test_zero_remainder(self):
        self.assertEqual(modulo(10, 5), 0)

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            modulo(None, 3)


class TestPower(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(power(2, 8), 256)

    def test_zero_exponent(self):
        self.assertEqual(power(99, 0), 1)

    def test_float_base(self):
        self.assertAlmostEqual(power(2.0, 3), 8.0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            power("2", 3)


class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(10, "+", 5), 15)

    def test_subtract(self):
        self.assertEqual(calculate(10, "-", 3), 7)

    def test_multiply(self):
        self.assertEqual(calculate(4, "*", 7), 28)

    def test_divide(self):
        self.assertAlmostEqual(calculate(20, "/", 4), 5.0)

    def test_floor_divide(self):
        self.assertEqual(calculate(20, "//", 3), 6)

    def test_modulo(self):
        self.assertEqual(calculate(20, "%", 3), 2)

    def test_power(self):
        self.assertEqual(calculate(2, "**", 8), 256)

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, "^", 2)

    def test_operator_type_error(self):
        with self.assertRaises(TypeError):
            calculate(1, 99, 2)  # type: ignore

    def test_zero_division_via_calculate(self):
        with self.assertRaises(ValueError):
            calculate(5, "/", 0)

    def test_type_error_via_calculate(self):
        with self.assertRaises(TypeError):
            calculate("a", "+", 1)


class TestSupportedOperators(unittest.TestCase):
    def test_contains_all(self):
        expected = {"+", "-", "*", "/", "//", "%", "**"}
        self.assertEqual(SUPPORTED_OPERATORS, expected)


if __name__ == "__main__":
    unittest.main()
