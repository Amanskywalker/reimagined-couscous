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

def test_multiple_numbers():
    """
    Test that multiple numbers separated by commas return their sum.
    """
    assert add("1,2,3,4") == 10

def test_new_lines_between_numbers():
    """
    Test that new lines can be used as delimiters in place of commas.
    """
    assert add("1\n2,3") == 6

def test_different_delimiters():
    """
    Test that a custom delimiter can be specified and used for separating numbers.
    """
    assert add("//;\n1;2") == 3
