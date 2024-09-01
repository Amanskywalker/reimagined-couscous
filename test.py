"""
Test.py
"""
from main import add

def test_empty_string():
    """
    Test that an empty string returns 0.
    """
    assert add("") == 0

def test_single_number():
    """
    Test that a single number string returns the number itself.
    """
    assert add("1") == 1

def test_two_numbers():
    """
    Test that two numbers separated by a comma return their sum.
    """
    assert add("1,2") == 3

