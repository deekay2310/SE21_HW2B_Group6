#import sys
import pytest
#sys.path.append("../Calculator")
from Calculator.Calculator import nth_root, logarithms

def test_nth_root():
    assert nth_root(3,2) == 9.0
    
def test_logarithm():
    assert logarithms(2,2) == 1.0

#test_nth_root() 
#test_logarithm()
