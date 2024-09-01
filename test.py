"""
Test.py
"""
import pytest

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

def test_negative_numbers():
    """
    Test that passing negative numbers raises a ValueError with all negatives listed.
    """
    with pytest.raises(ValueError) as excinfo:
        add("1,-2,3,-4")
    assert str(excinfo.value) == "negatives not allowed: -2, -4"

def test_ignore_numbers_greater_than_1000():
    """
    Test that numbers greater than 1000 are ignored in the sum.
    """
    assert add("2,1001") == 2

def test_delimiters_of_any_length():
    """
    Test that delimiters of any length can be used to separate numbers.
    """
    assert add("//[***]\n1***2***3") == 6

def test_multiple_delimiters():
    """
    Test that multiple custom delimiters can be used simultaneously.
    """
    assert add("//[*][%]\n1*2%3") == 6
