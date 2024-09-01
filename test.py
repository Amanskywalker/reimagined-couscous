import pytest

from main import add

def test_empty_string():
    assert add("") == 0