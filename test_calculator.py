import pytest
from calculator import add, subtract, multiply, divide, power

# ------------------- ADDITION TESTS -------------------
class TestAdd:
    def test_add_positive(self):
        print("Testing addition of two positive numbers")
        assert add(5, 7) == 12, "5 + 7 should equal 12"

    def test_add_negative(self):
        print("Testing addition of two negative numbers")
        assert add(-3, -6) == -9, "-3 + -6 should equal -9"

    def test_add_mixed(self):
        print("Testing addition of negative and positive number")
        assert add(-4, 6) == 2, "-4 + 6 should equal 2"

    def test_add_zero(self):
        print("Testing addition with zero")
        assert add(0, 5) == 5, "0 + 5 should equal 5"


# ------------------- SUBTRACTION TESTS -------------------
class TestSubtract:
    def test_subtract_positive(self):
        print("Testing subtraction of two positive numbers")
        assert subtract(10, 4) == 6, "10 - 4 should equal 6"

    def test_subtract_negative(self):
        print("Testing subtraction of two negative numbers")
        assert subtract(-5, -3) == -2, "-5 - -3 should equal -2"

    def test_subtract_mixed(self):
        print("Testing subtraction of negative from positive")
        assert subtract(3, -2) == 5, "3 - -2 should equal 5"

    def test_subtract_zero(self):
        print("Testing subtraction with zero")
        assert subtract(0, 7) == -7, "0 - 7 should equal -7"


# ------------------- MULTIPLICATION TESTS -------------------
class TestMultiply:
    def test_multiply_positive(self):
        print("Testing multiplication of two positive numbers")
        assert multiply(3, 4) == 12, "3 * 4 should equal 12"

    def test_multiply_negative(self):
        print("Testing multiplication of two negative numbers")
        assert multiply(-2, -5) == 10, "-2 * -5 should equal 10"

    def test_multiply_mixed(self):
        print("Testing multiplication of negative and positive number")
        assert multiply(-3, 6) == -18, "-3 * 6 should equal -18"

    def test_multiply_zero(self):
        print("Testing multiplication with zero")
        assert multiply(0, 100) == 0, "0 * 100 should equal 0"


# ------------------- DIVISION TESTS -------------------
class TestDivide:
    def test_divide_positive(self):
        print("Testing division of two positive numbers")
        assert divide(10, 2) == 5, "10 / 2 should equal 5"

    def test_divide_negative(self):
        print("Testing division of two negative numbers")
        assert divide(-9, -3) == 3, "-9 / -3 should equal 3"

    def test_divide_mixed(self):
        print("Testing division of negative by positive number")
        assert divide(-8, 2) == -4, "-8 / 2 should equal -4"

    def test_divide_zero_numerator(self):
        print("Testing division of zero by a number")
        assert divide(0, 5) == 0, "0 / 5 should equal 0"

    def test_divide_by_zero(self):
        print("Testing division by zero")
        with pytest.raises(ValueError, match="division by zero"):
            divide(5, 0)


# ------------------- POWER TESTS -------------------
class TestPower:
    def test_power_positive(self):
        print("Testing positive exponent")
        assert power(2, 3) == 8, "2 ** 3 should equal 8"

    def test_power_zero_exponent(self):
        print("Testing zero exponent")
        assert power(5, 0) == 1, "5 ** 0 should equal 1"

    def test_power_negative_exponent(self):
        print("Testing negative exponent")
        assert power(2, -2) == 0.25, "2 ** -2 should equal 0.25"
