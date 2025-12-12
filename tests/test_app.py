import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add

def test_add():
    assert add(5,6) == 11

def test_add2():
    assert add(5,6) != 10

def test_sub():
    assert subtract(10, 5) == 5

def test_sub2():
    assert subtract(11, 4) != 7

def test_mult():
    assert multiply(3,4) == 12

def test_mult2():
    assert multiply(2,7) == 14

def test_div():
    assert division(12,4) == 3

def test_div2():
    assert division(16, 4) != 7

