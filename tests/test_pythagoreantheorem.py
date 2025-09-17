from pythagoreantheorem import PythagoreanTheorem
import math

def test_pythagorean_3_4_5():
    """Test the classic 3-4-5 right triangle"""
    triangle = PythagoreanTheorem(3, 4)
    assert abs(triangle.hypotenuse() - 5.0) < 0.001

def test_pythagorean_5_12_13():
    """Test another classic right triangle"""
    triangle = PythagoreanTheorem(5, 12)
    assert abs(triangle.hypotenuse() - 13.0) < 0.001

def test_pythagorean_1_1():
    """Test with equal sides"""
    triangle = PythagoreanTheorem(1, 1)
    expected = math.sqrt(2)
    assert abs(triangle.hypotenuse() - expected) < 0.001

def test_pythagorean_6_8():
    """Test 6-8-10 right triangle"""
    triangle = PythagoreanTheorem(6, 8)
    assert abs(triangle.hypotenuse() - 10.0) < 0.001

def test_pythagorean_7_24():
    """Test 7-24-25 right triangle"""
    triangle = PythagoreanTheorem(7, 24)
    assert abs(triangle.hypotenuse() - 25.0) < 0.001

def test_pythagorean_9_12():
    """Test 9-12-15 right triangle"""
    triangle = PythagoreanTheorem(9, 12)
    assert abs(triangle.hypotenuse() - 15.0) < 0.001


def test_pythagorean_decimal_sides():
    """Test with decimal side lengths"""
    triangle = PythagoreanTheorem(1.5, 2.0)
    expected = math.sqrt(1.5**2 + 2.0**2)
    assert abs(triangle.hypotenuse() - expected) < 0.001
