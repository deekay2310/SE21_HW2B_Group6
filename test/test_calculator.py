import sys
import pytest
sys.path.append("../Calculator")
from Calculator import addition, subtraction, multiplication, division

def test_addition():
    assert addition(3,4) == 7.0
    
def test_subtraction():
    assert subtraction(3,4) == -1.0

def test_multiplication():
    assert multiplication(3,4) == 12.0

def test_division():
    assert division(3,4) == 0.75
    
test_addition()
test_subtraction()
test_multiplication()
test_division()
