# test_calculator.py
import pytest
from calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add('hello ', 'world') == 'hello world'
    assert add(0, 0) == 0
