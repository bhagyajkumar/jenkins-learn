import pytest
import time
import logging
from calculator import add, subtract, multiply, divide, power

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ------------------- ADDITION TESTS -------------------
class TestAdd:
    def test_add_positive(self):
        """Addition of two positive numbers"""
        logger.info("Testing addition: 5 + 7")
        time.sleep(0.1)
        assert add(5, 7) == 12, "5 + 7 should equal 12"

    def test_add_negative(self):
        """Addition of two negative numbers"""
        logger.info("Testing addition: -3 + -6")
        time.sleep(0.1)
        assert add(-3, -6) == -9, "-3 + -6 should equal -9"

    def test_add_mixed(self):
        """Addition of negative and positive number"""
        logger.info("Testing addition: -4 + 6")
        time.sleep(0.1)
        assert add(-4, 6) == 2, "-4 + 6 should equal 2"

    def test_add_zero(self):
        """Addition with zero"""
        logger.info("Testing addition: 0 + 5")
        time.sleep(0.1)
        assert add(0, 5) == 5, "0 + 5 should equal 5"

# ------------------- SUBTRACTION TESTS -------------------
class TestSubtract:
    def test_subtract_positive(self):
        """Subtraction of two positive numbers"""
        logger.info("Testing subtraction: 10 - 4")
        time.sleep(0.1)
        assert subtract(10, 4) == 6, "10 - 4 should equal 6"

    def test_subtract_negative(self):
        """Subtraction of two negative numbers"""
        logger.info("Testing subtraction: -5 - -3")
        time.sleep(0.1)
        assert subtract(-5, -3) == -2, "-5 - -3 should equal -2"

    def test_subtract_mixed(self):
        """Subtraction of negative from positive"""
        logger.info("Testing subtraction: 3 - -2")
        time.sleep(0.1)
        assert subtract(3, -2) == 5, "3 - -2 should equal 5"

    def test_subtract_zero(self):
        """Subtraction with zero"""
        logger.info("Testing subtraction: 0 - 7")
        time.sleep(0.1)
        assert subtract(0, 7) == -7, "0 - 7 should equal -7"

# ------------------- MULTIPLICATION TESTS -------------------
class TestMultiply:
    def test_multiply_positive(self):
        """Multiplication of two positive numbers"""
        logger.info("Testing multiplication: 3 * 4")
        time.sleep(0.1)
        assert multiply(3, 4) == 12, "3 * 4 should equal 12"

    def test_multiply_negative(self):
        """Multiplication of two negative numbers"""
        logger.info("Testing multiplication: -2 * -5")
        time.sleep(0.1)
        assert multiply(-2, -5) == 10, "-2 * -5 should equal 10"

    def test_multiply_mixed(self):
        """Multiplication of negative and positive number"""
        logger.info("Testing multiplication: -3 * 6")
        time.sleep(0.1)
        assert multiply(-3, 6) == -18, "-3 * 6 should equal -18"

    def test_multiply_zero(self):
        """Multiplication with zero"""
        logger.info("Testing multiplication: 0 * 100")
        time.sleep(0.1)
        assert multiply(0, 100) == 0, "0 * 100 should equal 0"

# ------------------- DIVISION TESTS -------------------
class TestDivide:
    def test_divide_positive(self):
        """Division of two positive numbers"""
        logger.info("Testing division: 10 / 2")
        time.sleep(0.1)
        assert divide(10, 2) == 5, "10 / 2 should equal 5"

    def test_divide_negative(self):
        """Division of two negative numbers"""
        logger.info("Testing division: -9 / -3")
        time.sleep(0.1)
        assert divide(-9, -3) == 3, "-9 / -3 should equal 3"

    def test_divide_mixed(self):
        """Division of negative by positive number"""
        logger.info("Testing division: -8 / 2")
        time.sleep(0.1)
        assert divide(-8, 2) == -4, "-8 / 2 should equal -4"

    def test_divide_zero_numerator(self):
        """Division of zero by a number"""
        logger.info("Testing division: 0 / 5")
        time.sleep(0.1)
        assert divide(0, 5) == 0, "0 / 5 should equal 0"

# ------------------- POWER TESTS -------------------
class TestPower:
    def test_power_positive(self):
        """Positive exponent"""
        logger.info("Testing power: 2 ** 3")
        time.sleep(0.1)
        assert power(2, 3) == 8, "2 ** 3 should equal 8"

    def test_power_zero_exponent(self):
        """Zero exponent"""
        logger.info("Testing power: 5 ** 0")
        time.sleep(0.1)
        assert power(5, 0) == 1, "5 ** 0 should equal 1"

    def test_power_negative_exponent(self):
        """Negative exponent"""
        logger.info("Testing power: 2 ** -2")
        time.sleep(0.1)
        assert power(2, -2) == 0.25, "2 ** -2 should equal 0.25"
