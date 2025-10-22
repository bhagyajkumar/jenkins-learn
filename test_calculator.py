import pytest
from calculator import add, subtract, multiply, divide, power

# ------------------- ADDITION TESTS -------------------
class TestAdd:
    def test_add_positive(self):
        assert add(5, 7) == 12

    def test_add_negative(self):
        assert add(-3, -6) == -9

    def test_add_mixed(self):
        assert add(-4, 6) == 2

    def test_add_zero(self):
        assert add(0, 5) == 5


# ------------------- SUBTRACTION TESTS -------------------
class TestSubtract:
    def test_subtract_positive(self):
        assert subtract(10, 4) == 6

    def test_subtract_negative(self):
        assert subtract(-5, -3) == -2

    def test_subtract_mixed(self):
        assert subtract(3, -2) == 5

    def test_subtract_zero(self):
        assert subtract(0, 7) == -7


# ------------------- MULTIPLICATION TESTS -------------------
class TestMultiply:
    def test_multiply_positive(self):
        assert multiply(3, 4) == 12

    def test_multiply_negative(self):
        assert multiply(-2, -5) == 10

    def test_multiply_mixed(self):
        assert multiply(-3, 6) == -18

    def test_multiply_zero(self):
        assert multiply(0, 100) == 0


# ------------------- DIVISION TESTS -------------------
class TestDivide:
    def test_divide_positive(self):
        assert divide(10, 2) == 5

    def test_divide_negative(self):
        assert divide(-9, -3) == 3

    def test_divide_mixed(self):
        assert divide(-8, 2) == -4

    def test_divide_zero_numerator(self):
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(5, 0)


# ------------------- POWER TESTS -------------------
class TestPower:
    def test_power_positive(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -2) == 0.25
