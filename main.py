"""
Main.py
it contains Add function for the string calculator
"""

import re

def add(numbers: str) -> int:
    """
    Calculate the sum of numbers provided in a string.
    
    The string can contain numbers separated by commas or new lines. 
    Custom delimiters can be specified in the format `//[delimiter]\n`.
    The function handles:
    - An empty string (returns 0)
    - A single number (returns the number itself)
    - Multiple numbers separated by commas or new lines
    - Custom delimiters of any length
    - Negative numbers (raises an exception with all negative numbers listed)

    Args:
        numbers (str): A string containing numbers separated by delimiters.

    Returns:
        int: The sum of the numbers in the string.

    Raises:
        ValueError: If negative numbers are found in the string.
    """
    if not numbers:
        return 0
    
    if numbers.startswith("//"):
        delimiter, numbers = re.match(r"//(.)\n(.*)", numbers).groups()
        numbers = numbers.replace(delimiter, ',')
    
    numbers = numbers.replace('\n', ',')
    nums = list(map(int, numbers.split(',')))

    # Check for negative numbers
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    return sum(nums)