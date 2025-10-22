import pytest
from calculator import add, subtract, multiply, divide, power
import time

# ------------------- ADDITION TESTS -------------------
class TestAdd:
    def test_add_positive(self):
        time.sleep(1000)
        assert add(5, 7) == 12

    def test_add_negative(self):
        time.sleep(1000)
        assert add(-3, -6) == -9

    def test_add_mixed(self):
        time.sleep(1000)
        assert add(-4, 6) == 2

    def test_add_zero(self):
        time.sleep(1000)
        assert add(0, 5) == 5


# ------------------- SUBTRACTION TESTS -------------------
class TestSubtract:
    def test_subtract_positive(self):
        time.sleep(1000)
        assert subtract(10, 4) == 6

    def test_subtract_negative(self):
        time.sleep(1000)
        assert subtract(-5, -3) == -2

    def test_subtract_mixed(self):
        time.sleep(1000)
        assert subtract(3, -2) == 5

    def test_subtract_zero(self):
        time.sleep(1000)
        assert subtract(0, 7) == -7


# ------------------- MULTIPLICATION TESTS -------------------
class TestMultiply:
    def test_multiply_positive(self):
        time.sleep(1000)
        assert multiply(3, 4) == 12

    def test_multiply_negative(self):
        time.sleep(1000)
        assert multiply(-2, -5) == 10

    def test_multiply_mixed(self):
        time.sleep(1000)
        assert multiply(-3, 6) == -18

    def test_multiply_zero(self):
        time.sleep(1000)
        assert multiply(0, 100) == 0


# ------------------- DIVISION TESTS -------------------
class TestDivide:
    def test_divide_positive(self):
        time.sleep(1000)
        assert divide(10, 2) == 5

    def test_divide_negative(self):
        time.sleep(1000)
        assert divide(-9, -3) == 3

    def test_divide_mixed(self):
        time.sleep(1000)
        assert divide(-8, 2) == -4

    def test_divide_zero_numerator(self):
        time.sleep(1000)
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        time.sleep(1000)
        with pytest.raises(ValueError):
            divide(5, 0)


# ------------------- POWER TESTS -------------------
class TestPower:
    def test_power_positive(self):
        time.sleep(1000)
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        time.sleep(1000)
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        time.sleep(1000)
        assert power(2, -2) == 0.25
