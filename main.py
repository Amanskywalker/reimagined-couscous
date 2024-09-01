"""
Main.py
It contains the `add` function for the string calculator.
"""

import re
from typing import List

def add(numbers: str) -> int:
    """
    Calculate the sum of numbers provided in a string.

    The string can contain numbers separated by commas, new lines, or custom delimiters. 
    Custom delimiters can be specified in the format `//[delimiter]\n` or `//delimiter\n`.
    The function handles:
    - An empty string (returns 0)
    - A single number (returns the number itself)
    - Multiple numbers separated by commas or new lines
    - Custom delimiters of any length
    - Negative numbers (raises an exception with all negative numbers listed)
    - Numbers greater than 1000 (ignored in the sum)

    Args:
        numbers (str): A string containing numbers separated by delimiters.

    Returns:
        int: The sum of the numbers in the string.

    Raises:
        ValueError: If negative numbers are found in the string.
    """
    if not numbers:
        return 0
   
    delimiter = ','
    numbers = numbers.strip()
 
    if numbers.startswith("//"):
        delimiter, numbers = _extract_delimiter_and_numbers(numbers)

    # Replace new lines with the delimiter and split by the delimiter
    number_list = _split_numbers(numbers, delimiter)

    # Convert to integers, ignoring numbers > 1000
    nums = _convert_to_integers(number_list)

    # Check for negative numbers
    _validate_no_negatives(nums)

    return sum(nums)

def _extract_delimiter_and_numbers(numbers: str) -> (str, str):
    """
    Extract custom delimiters and the remaining numbers from the input string.
    """
    custom_delimiter_pattern = r"//(\[.*\])\n(.*)"
    simple_delimiter_pattern = r"//(.)\n(.*)"
 
    match = re.match(custom_delimiter_pattern, numbers)
    if match:
        delimiters, numbers = match.groups()
        delimiters = re.findall(r'\[(.*?)\]', delimiters)
        for delim in delimiters:
            numbers = numbers.replace(delim, ',')
        return ',', numbers
    else:
        match = re.match(simple_delimiter_pattern, numbers)
        if match:
            return match.groups()

    return ',', numbers

def _split_numbers(numbers: str, delimiter: str) -> List[str]:
    """
    Split the input string into a list of numbers using the specified delimiter.
    """
    return numbers.replace('\n', delimiter).split(delimiter)

def _convert_to_integers(number_list: List[str]) -> List[int]:
    """
    Convert a list of numeric strings to integers, ignoring numbers > 1000.
    """
    return [int(num) for num in number_list if int(num) <= 1000]

def _validate_no_negatives(nums: List[int]):
    """
    Check if the list of numbers contains any negatives. Raise an exception if so.
    """
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
