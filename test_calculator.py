import pytest
from calculator import add, subtract, multiply, divide, power

# --- ADDITION TESTS ---
def test_add_positive():
    assert add(5, 7) == 12

def test_add_negative():
    assert add(-3, -6) == -9

def test_add_mixed():
    assert add(-4, 6) == 2

def test_add_zero():
    assert add(0, 5) == 5

# --- SUBTRACTION TESTS ---
def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-5, -3) == -2

def test_subtract_mixed():
    assert subtract(3, -2) == 5

def test_subtract_zero():
    assert subtract(0, 7) == -7

# --- MULTIPLICATION TESTS ---
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_negative():
    assert multiply(-2, -5) == 10

def test_multiply_mixed():
    assert multiply(-3, 6) == -18

def test_multiply_zero():
    assert multiply(0, 100) == 0

# --- DIVISION TESTS ---
def test_divide_positive():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-9, -3) == 3

def test_divide_mixed():
    assert divide(-8, 2) == -4

def test_divide_zero_numerator():
    assert divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

# --- POWER TESTS ---
def test_power_positive():
    assert power(2, 3) == 8

def test_power_zero_exponent():
    assert power(5, 0) == 1

def test_power_negative_exponent():
    assert power(2, -2) == 0.25
